from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError('price must be > 0')
        return price


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('slug', 'title', 'price', 'image',)
