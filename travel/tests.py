from django.urls import path
from .views import TouristListView, TouristDetailView

urlpatterns = [
    path('', TouristListView.as_view(), name='tourist_list'),
    path('<int:pk>/', TouristDetailView.as_view(), name='tourist_detail'),
]



