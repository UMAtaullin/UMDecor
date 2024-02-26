from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Название категории")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150, unique=True, verbose_name="Название категории")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True,
        verbose_name="Изображение")
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(
        default=0.00, max_digits=2, decimal_places=0, verbose_name="Скидка %")
    quantity = models.PositiveIntegerField(
        default=0, verbose_name="Количество")
    cat = models.ForeignKey(
        to=Category, on_delete=models.PROTECT, verbose_name="Категория")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price
