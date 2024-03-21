from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


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
                messages.success(request, f"{username}, Вы вошли в аккаунт.")
                return HttpResponseRedirect(reverse("main:index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserLoginForm()

    data = {
        "title": "Home - Авторизация",
        "form": form}

    return render(request, "users/login.html", data)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(
                request, f"{user.username}, Вы успешно зарегистрировались.")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    data = {
        "title": "Home - Регистрация",
        "form": form,
        }

    return render(request, "users/registration.html", data)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен.")
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = ProfileForm(instance=request.user)

    data = {
        "title": "Home - Кабинет",
        "form": form,
        }

    return render(request, "users/profile.html", data)


@login_required()
def logout(request):
    messages.success(
        request, f"{request.user.username}, Вы вышли из аккаунта.")
    auth.logout(request)
    return redirect(reverse("main:index"))
