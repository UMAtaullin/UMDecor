from django.shortcuts import render

from goods.models import Category


def index(request):

    data = {
        "title": "UMHome - Главная",
        "content": "Магазин мебели",
    }
    return render(request, "main/index.html", data)


def about(request):
    data = {
        "title": "UMHome - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том, какой у нас классный магазин",
    }
    return render(request, "main/about.html", data)
