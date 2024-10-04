from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    GENDER_CHOICES = [
        ('M', '남'),
        ('F', '여'),
        ('O', '기타'),
    ]

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)  # 지도 API와 연동될 주소 필드
    image = models.ImageField(upload_to='documents/', blank=True, null=True)  # 사진 업로드
    birthdate = models.DateField(blank=True, null=True)  # 생년월일 필드 추가
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)  # 성별 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
        ]

    def __str__(self):
        return self.title
