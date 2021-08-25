from django.urls import path

from product.api.views import CategoriesAPIView, CategoryAPIView,ProductAPIView,ProductDetailAPIView, LikedItemsAPIView

app_name='product_api'

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category_detail'),

    path('products/',ProductAPIView.as_view(),name='products'),
    path('products/<int:pk>/',ProductDetailAPIView.as_view(),name='product_detail'),

    path('likeditems/', LikedItemsAPIView.as_view(), name='likeditems'),
    path('likeditems/<int:pk>/', LikedItemsAPIView.as_view(), name='likeditem'),

]
