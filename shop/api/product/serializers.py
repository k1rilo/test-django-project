from .models import Product
from rest_framework import serializers
from api.cart.serializers import CartSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price',
                  'category', 'imageUrl', 'stockquantity')
        

class ProductDetailSerializer(serializers.ModelSerializer):
    carts_product = CartSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price',
                  'category', 'imageUrl', 'stockquantity', 'carts_product')