from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.CharField(max_length=100)  # 게시글 작성자
    title = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)  # 지도 API와 연동될 주소 필드
    image = models.ImageField(upload_to='documents/', blank=True, null=True)  # 사진 업로드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
    permissions = [
        ("change_post", "Can change the post"),
        ("delete_post", "Can delete the post"),
    ]

    def __str__(self):
        return self.title
