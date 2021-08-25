from rest_framework import serializers
from product.models import Category, Product, Tag, Wishlist



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'is_published',

        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'is_published',
             )



class CategoryListSerializer(CategorySerializer):
        class Meta:
            model = Category
            fields = (
            'id',
            'title',
            'is_published',
            
            )




class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            
            'name',
            'created_at',

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

    

class ProductListSerializer(ProductSerializer):

    category=CategorySerializer()
    tag=TagSerializer(many=True)



   
class LikedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            'id',
            'user',
            'product'
        )


class LikedItemListSerializer(LikedItemSerializer):
    product=ProductSerializer()


