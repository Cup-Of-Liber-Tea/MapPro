from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import homework1,homework2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include('user.urls')),
    path("", include('users.urls')),     ############ 추가 함(남승수)
    path("travel/", include('travel.urls')),
    path("data/", include('data.urls')),
    path("work1/", homework1), 
    path("work2/", homework2), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)