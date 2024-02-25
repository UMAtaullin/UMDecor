from django.shortcuts import render

from goods.models import Category


def index(request):

    categories = Category.objects.all()

    data = {
        "title": "UMHome - Главная",
        "content": "Магазин мебели",
        "categories": categories
    }
    return render(request, "main/index.html", data)


def about(request):
    data = {
        "title": "UMHome - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том, какой у нас классный магазин",
    }
    return render(request, "main/about.html", data)
