from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    # Если это запрос POST, нам необходимо обработать данные формы.
    if request.method == "POST":
        # Создайте экземпляр формы и заполните его данными из запроса:
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = request.POST['username']
            password = request.POST['password']
            # auth.authenticate проверяет есть ли такой пользователь в БД.
            user = auth.authenticate(
                username=username, password=password)
            if user:
                # auth.login для авторизации пользователя.
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserLoginForm()

    data = {
        "title": "Home - Авторизация",
        "form": form}

    return render(request, "users/login.html", data)


def registration(request):

    data = {"title": "Home - Регистрация"}

    return render(request, "users/registration.html", data)


def profile(request):

    data = {"title": "Home - Кабинет"}

    return render(request, "users/profile.html", data)


def logout(request):

    pass
