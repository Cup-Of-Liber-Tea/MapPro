from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm


def login_signup_view(request):
    if request.user.is_authenticated:
        return redirect("/user/")

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        signup_form = SignupForm(request.POST)
        if login_form.is_valid():
            # 로그인 처리 로직
            username = login_form.cleaned_data["아이디"]
            password = login_form.cleaned_data["비밀번호"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("/user/")
            # else:
            #     login_form.add_error(None, "로그인 실패. 다시 입력해주세요")

        elif signup_form.is_valid():
            # 회원가입 처리 로직
            user = signup_form.save()
            login(request, user)
            success_message = "회원가입이 완료되었습니다."
            # return redirect("/user/")


    else:
        login_form = LoginForm()
        signup_form = SignupForm()

    return render(request, 'login.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })


def logout_view(request):
    logout(request)

    return redirect("/users/login/")