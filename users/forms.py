from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    # username = forms.CharField()
    # password = forms.CharField()

    # username = forms.CharField(
    #     label='Имя',
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Введите имя пользователя",
    #         }
    #     )
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autocomplete": "current-password",
    #             "class": "form-control",  # помогает создать красивые формы.
    #             "placeholder": "Введите ваш пароль",
    #         }
    #     ),
    # )


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
