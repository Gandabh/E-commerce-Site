from django.urls import path

from core.api.views import  SubscribeAPIView,CartItemsAPIView

app_name = 'core_api'

urlpatterns = [
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('cartitems/', CartItemsAPIView.as_view(), name='cartitems'),
    path('cartitems/<int:pk>/', CartItemsAPIView.as_view(), name='basket_detail'),


]