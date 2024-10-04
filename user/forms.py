from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'location', 'image', 'birthdate', 'gender']  # 생년월일 포함
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),  # HTML에서 date 형식으로 표시
        }
