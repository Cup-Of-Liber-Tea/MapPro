from django.contrib.admin import views
from django.urls import path
from .views import travel_stats_view
urlpatterns = [
    path("", travel_stats_view, name='travel_stats_view'),

 ]
