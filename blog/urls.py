from django.urls import path,include
from blog.views import (
    BlogView,
    BlogDetailView,

)


app_name = 'blog'
urlpatterns = [
    path('blog-list',BlogView.as_view(), name='blog_list'),
    path('blog-detail/<slug:slug>',BlogDetailView.as_view(), name='blog_detail'),



]