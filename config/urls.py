from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("catalog/", include("goods.urls", namespace="catalog")),
    path("__debug__/", include("debug_toolbar.urls")),
]


"""
www.site.com/admin/
www.site.com
www.site.com/about/
www.site.com/catalog/
www.site.com/catalog/product
"""
