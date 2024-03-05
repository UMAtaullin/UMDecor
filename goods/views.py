from django.shortcuts import get_list_or_404, render

from goods.models import Product


def catalog(request, category_slug):

    if category_slug == "all":
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(cat__slug=category_slug))

    data = {"title": "Home - Catalog", "goods": goods}
    return render(request, "goods/catalog.html", data)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    data = {"product": product}
    return render(request, "goods/product.html", data)
