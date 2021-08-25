from rest_framework import serializers
from core.models import  Subscriber
from product.models import CartItems, Product

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields=(
            'id',
            'title',
            'description',
            'count',
            'category',
            'information',
            'price',
            'designer',
            'brand',
            'tag',
            'cover_image',
            'discount',
            'created_at',
            'updated_at',
        )


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = (
            'id',
            'user',
            'product',
            'quantity',
            'color'
        )

class BasketListSerializer(BasketSerializer):
    product=ProductSerializer()
