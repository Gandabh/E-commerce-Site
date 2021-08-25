from django.contrib import admin

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import (
    Product,
    Review, 
    Category,
    Color,
    Brand,
    Tag,
    Image,
    CartItems,
    Wishlist
)



@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user','product','created_at')
    list_filter = ('user','product','created_at')
    search_fields = ('user','product','created_at')



@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity','color')
    list_filter = ('user','product','quantity')
    search_fields = ('user','product','quantity')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','is_published')
    list_filter = ('title','is_published')
    search_fields = ('title','is_published')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product','title','product','is_published')
    list_filter = ('title','product','is_published')
    search_fields = ('title','product','is_published')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title','is_published')
    list_filter = ('title','is_published')
    search_fields = ('title','is_published')



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','is_published')
    list_filter = ('name','is_published')
    search_fields = ('name','is_published')


class CategoryAdmin(TranslationAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','is_published')
    list_filter = ('title','is_published')
    search_fields = ('title','is_published')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','content','product','rate','is_published')
    list_filter = ('user','content','rate','is_published')
    search_fields = ('user','content','rate','is_published')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','category','get_avg_rating','is_published','created_at')  
    list_filter = ('title','description','price','category','is_published','created_at','updated_at')
    search_fields = ('title','description','price','category','is_published')