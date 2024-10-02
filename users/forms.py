from django import forms
from .models import User
from django.core.exceptions import ValidationError  # ValidationError를 추가로 import
class LoginForm(forms.Form):
    아이디 = forms.CharField(
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "사용자명",
                "autocomplete": "off",
                "name": "아이디",

                "class": "input"
                   }

        )

    )
    비밀번호 = forms.CharField(
        min_length=4,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "비밀번호",
                "autocomplete": "off",
                "name": "비밀번호",
                "class": "input",
                }
        )
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,

    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다.")
        return username

    def clean(self):
        cleaned_data = super().clean()  # cleaned_data를 먼저 불러옴
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인이 일치하지 않습니다.")

        return cleaned_data

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]

        user = User.objects.create_user(
            username=username,
            password=password1,  # 비밀번호는 여기서 자동으로 해시됨
        )
        return user