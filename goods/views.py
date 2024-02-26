from django.shortcuts import render

from goods.models import Product


def catalog(request):
    goods = Product.objects.all()
    data = {
        "title": "Home - Catalog",
        "goods": goods
    }
    return render(request, "goods/catalog.html", data)


def product(request):
    return render(request, "goods/product.html")
