from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = (
            'id',
            'image',
            'title',
            'description',
            'price')
