from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'category',
                    'url',
                    'desc',
                    'price']
    search_fields = ['name', 'category']
    list_filter = ['category']

    ordering = ['id']


admin.site.register(Product, ProductAdmin)
