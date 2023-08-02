from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'image',
                    'description',
                    'price']

    ordering = ['id']


admin.site.register(Product, ProductAdmin)
