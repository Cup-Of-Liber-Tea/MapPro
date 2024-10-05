from django.shortcuts import render
from user.models import Post
from django.db.models.functions import ExtractYear
from django.db.models import Count
from django.shortcuts import render
import pandas as pd
import datetime
from django.db.models import Case, When, IntegerField
def travel_stats_view(request):
    # 여행지별 리뷰 수
    destination_stats = Post.objects.values('title').annotate(count=Count('title')).order_by('-count')

    # 작성자, 제목열을 가진 데이터프레임
    reviews = Post.objects.all().values('author', 'title')  # 작성자와 리뷰 ID
    df = pd.DataFrame(reviews)

    # 작성자기준으로 그룹바이해서 행의수를 합친 데이터프레임
    author_stats = df.groupby('author').size().reset_index(name='count')

    # 성별 리뷰 수
    gender_stats = Post.objects.values('gender').annotate(count=Count('gender'))



    #나이 분석 파트
    # 현재 연도
    current_year = datetime.datetime.now().year

    # 나이별 통계 계산
    birthdate_stats = Post.objects.annotate(
        year=Case(
            When(birthdate__isnull=False, then=ExtractYear('birthdate')),
            default=None,
            output_field=IntegerField()
        )
    ).values('year').annotate(count=Count('title')).order_by('-count')

    print(birthdate_stats)


    # 나이를 계산하여 데이터프레임 생성
    age_stats = []
    for stat in birthdate_stats:
        if stat['year'] is not None:  # year가 None이 아닐 때만 처리
            age = current_year - stat['year']  # 나이 계산
            age_stats.append({'age': age, 'count': stat['count']})

    # 데이터프레임으로 변환
    age_df = pd.DataFrame(age_stats)





    # 템플릿에 전달할 데이터 준비
    author_list = author_stats['author'].tolist()
    review_counts = author_stats['count'].tolist()
    gender_labels = [item['gender'] for item in gender_stats]
    gender_counts = [item['count'] for item in gender_stats]

    context = {
        'destination_stats': destination_stats,
        'author_stats': author_stats.to_dict('records'),  # 템플릿에 사용할 작성자 리뷰 통계
        'author_list': author_list,  # Chart.js에서 사용할 작성자 이름 리스트
        'review_counts': review_counts,  # Chart.js에서 사용할 리뷰 개수 리스트
        'gender_labels': gender_labels,
        'gender_counts': gender_counts,
        'gender_stats': gender_stats,
        'birthdate_stats': birthdate_stats,
        'age_df': age_df.to_dict('records'),

    }

    return render(request, 'travel_stats.html', context)