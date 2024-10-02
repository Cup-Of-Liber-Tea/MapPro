from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy
from travel.models import Tourist

class TouristListView(ListView):
    model = Tourist
    template_name = 'tourist_list.html'
    context_object_name = "tourist_list"
    paginate_by = 9

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

class TouristDetailView(DetailView):
    model = Tourist
    template_name = 'tourist_detail.html'
