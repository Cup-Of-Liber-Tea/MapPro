from django.urls import path
from .views import TouristListView, TouristDetailView
from user.views import PostDetailView

urlpatterns = [
    path('', TouristListView.as_view(), name='tourist_list'),
    path('<int:pk>/', TouristDetailView.as_view(), name='tourist_detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]



