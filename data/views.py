from django.shortcuts import render
from user.models import Post
# Create your views here.


from django.db.models import Count
from django.shortcuts import render


def travel_stats_view(request):
    # 여행지별 리뷰 수를 집계
    destination_stats = Post.objects.values('title').annotate(count=Count('title')).order_by('-count')

    context = {'destination_stats': destination_stats}
    return render(request, 'travel_stats.html', context)
