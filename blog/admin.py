from django.contrib import admin
from blog.models import Comment,Post,Tag
from account.models import User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'image','user','category','is_published','created_at','updated_at')  
    list_filter = ('image', 'title','user','is_published','created_at','category')
    search_fields = ('image', 'title','user','is_published','created_at','category')

    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name','is_published','created_at','updated_at')  
    list_filter = ('tag_name','is_published','created_at')
    search_fields = ('tag_name','is_published','created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','user','blog','parent_id','is_published','created_at','updated_at')  
    list_filter = ('blog','is_published','created_at')
    search_fields = ('blog','is_published','created_at')


