from django.shortcuts import render


def login(request):

    data = {"title": "Home - Авторизация"}

    return render(request, "users/login.html", data)


def registration(request):

    data = {"title": "Home - Регистрация"}

    return render(request, "users/registration.html", data)


def profile(request):

    data = {"title": "Home - Кабинет"}

    return render(request, "users/profile.html", data)


def logout(request):

    pass
