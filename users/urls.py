
from django.urls import path, include
from .views import  logout_view, login_signup_view

urlpatterns = [

    path("", login_signup_view, name='login_signup_view'),
    path("users/login/", login_signup_view, name='login_signup_view'),
    path("logout/", logout_view, name='logout'),

]
