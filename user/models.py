from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  

class Post(models.Model):
    TITLE_CHOICES = [
    ('mcy파크', 'mcy파크'),
    ('감포항', '감포항'),
    ('감포해국길', '감포해국길'),
    ('경주 남산 늠비봉오층석탑', '경주 남산 늠비봉오층석탑'),
    ('경주 남산 신선암 마애보살반가상', '경주 남산 신선암 마애보살반가상'),
    ('경주 동궁원', '경주 동궁원 Review'),
    ('경주 스파월드', 'Hotel 경주 스파월드'),
    ('경주 월성', 'Activity 경주 월성'),
    ('경주 풍력발전(바람의언덕)', '경주 풍력발전(바람의언덕)'),
    ('경주생활체육공원', '경주생활체육공원'),
    ('교촌마을', '교촌마을'),
    ('기림사', '기림사'),
    ('mcy파크', 'Trip mcy파크'),
    ('남산 불곡 마애여래좌상 (부처골 감실여래좌상)', '남산 불곡 마애여래좌상 (부처골 감실여래좌상)'),
    ('노서동 고분군', '노서동 고분군'),
    ('독락당', '독락당'),
    ('동궁과 월지', '동궁과 월지'),
    ('동대봉산 무장봉(억새군락지)', '동대봉산 무장봉(억새군락지)'),
    ('동리목월문학관', '동리목월문학관'),
    ('무열왕릉', '무열왕릉'),
    ('보리사', '보리사'),
    ('보문관광단지', '보문관광단지'),
    ('보문정', '보문정'),
    ('보문호반길', '보문호반길'),
    ('mcy파크', 'Trip mcy파크'),
    ('불국사', '불국사'),
    ('비단벌레 전기자동차', '비단벌레 전기자동차'),
    ('산내 동창천', '산내 동창천'),
    ('서악서원', '서악서원'),
    ('선덕여왕릉', '선덕여왕릉'),
    ('성동시장', '성동시장'),
    ('소노벨 경주 오션플레이', '소노벨 경주 오션플레이'),
    ('숭혜전', '숭혜전'),
    ('애니멀테마파크 주렁주렁', '애니멀테마파크 주렁주렁'),
    ('오류캠핑장', '오류캠핑장'),
    ('오봉산', '오봉산'),
    ('전촌항', '전촌항'),
    ('정글의법칙 미디어파크', '정글의법칙 미디어파크'),
    ('종오정 일원', '종오정 일원'),
    ('천군동 동서삼층석탑', '천군동 동서삼층석탑'),
    ('칠불암', '	칠불암'),
    ('포석정', '포석정'),
    ('황룡사지', '황룡사지'),
    ('흥덕왕릉', '흥덕왕릉'),
    ('히어로 키즈파크', '히어로 키즈파크'),
    ('양동마을', '양동마을'),
    ('황성공원', '황성공원'),
    ('탈해왕릉', '탈해왕릉'),

    ]
    GENDER_CHOICES = [
        ('M', '남'),
        ('F', '여'),
        ('O', '기타'),
    ]
    
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    sele = models.CharField(choices=TITLE_CHOICES ,max_length=100, blank=True, null=True)
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

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})