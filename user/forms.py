from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','sele', 'content', 'location', 'image', 'birthdate', 'gender']  # 생년월일 포함
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),  # HTML에서 date 형식으로 표시
            'sele': forms.Select(choices=Post.TITLE_CHOICES),  # sele 필드를 위한 Select 위젯 추가
        }
