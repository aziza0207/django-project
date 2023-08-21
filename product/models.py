from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    url = models.ImageField(null=True, blank=True, verbose_name="Изображение")
    name = models.CharField(max_length=50, verbose_name="Название")
    desc = models.CharField(max_length=255, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                verbose_name="Цена")
    wishlist = models.ManyToManyField(User, related_name='product_wishlist',
                                      blank=True, default=None, verbose_name="Избранное")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
