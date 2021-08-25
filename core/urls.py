from django.urls import path,include
from core.views import (
    reviews,
    comments,
    product_search,
    blog_post,
    IndexView,
    ContactView,
    AboutView


)


app_name='core'
urlpatterns = [
    path('reviews',reviews,name='reviews'),
    path('comments',comments,name='comments'),
    path('product-search',product_search,name='product_search'),
    path('blog-post',blog_post,name='blog_post'),
    path('',  IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-us/', AboutView.as_view(), name='about_us'),
   

]
