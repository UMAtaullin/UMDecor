from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
]

"""
www.site.com/admin/
www.site.com
www.site.com/about/
www.site.com/catalog/
www.site.com/catalog/product
"""
