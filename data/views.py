from django.shortcuts import render
from user.models import Post
# Create your views here.


from django.db.models import Count
from django.shortcuts import render
import pandas as pd

def travel_stats_view(request):
    # 여행지별 리뷰 수
    destination_stats = Post.objects.values('title').annotate(count=Count('title')).order_by('-count')

    # 작성자별 리뷰 수 계산 (데이터프레임 사용)
    reviews = Post.objects.all().values('author', 'title')  # 작성자와 리뷰 ID
    df = pd.DataFrame(reviews)

    # 작성자별 리뷰 수
    author_stats = df.groupby('author').size().reset_index(name='count')

    # 그래프에 필요한 데이터를 리스트로 변환
    author_names = author_stats['author'].tolist()
    review_counts = author_stats['count'].tolist()

    context = {
        'destination_stats': destination_stats,
        'author_stats': author_stats.to_dict('records'),  # 템플릿에 사용할 작성자 리뷰 통계
        'author_names': author_names,  # Chart.js에서 사용할 작성자 이름 리스트
        'review_counts': review_counts,  # Chart.js에서 사용할 리뷰 개수 리스트
    }

    return render(request, 'travel_stats.html', context)