from django.urls import path,include
from product.views import (
    ProductDetailView,
    ProductView,
    shopping_cart,
    wishlist


)


app_name='product'
urlpatterns = [
    path('product-detail/<int:pk>/', ProductDetailView.as_view(),name='product_detail'),
    path('product-list/', ProductView.as_view(),name='product_list'),
    path('shopping-cart/', shopping_cart,name='shopping_cart'),
    path('wishlist/', wishlist,name='wishlist'),


]
