from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy
from travel.models import Tourist

class TouristListView(ListView):
    model = Tourist
    template_name = 'tourist_list.html'
    context_object_name = "tourist_list"
    paginate_by = 6

    def get_queryset(self): # 검색할 경우 필터링된 쿼리셋 반환
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

from user.models import Post  # 사용자 리뷰 모델

class TouristDetailView(DetailView):
    model = Tourist
    template_name = 'tourist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user_post 테이블에서 현재 관광지와 관련된 리뷰를 필터링하여 전달
        context['reviews'] = Post.objects.filter(title=self.object.name)  # 제목이 관광지 이름과 일치하는 리뷰 가져오기
        return context