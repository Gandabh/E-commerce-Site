from django.db.models.aggregates import Count
from blog.models import *
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from blog.forms import CommentForm
from django.contrib.auth import authenticate, login as django_login
from account.models import User
from django.contrib import messages
from blog.models import Comment
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
import datetime
from.filters import PostFilter
from django.core.paginator import Paginator



class BlogDetailView(FormMixin,DetailView):
    
    model=Post
    template_name='blog-detail.html'
    form_class=CommentForm


    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['my_blog']=Post.objects.get(slug=self.kwargs['slug'])
        context['comment_list']=Comment.objects.all()
        context['recent_list']=Post.objects.all().order_by('created_at')[:4]
        context['tag_list']=Tag.objects.all()  
        context['blog_list']=Post.objects.all()[:4]
        context['category_list']=Category.objects.all()
        context['popular_tags']=Tag.objects.annotate(num_rev=Count('post'))[:3]
        context['filter']=PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def form_valid(self,form):
        form.instance.user = self.request.user
        comment = form.save(commit=False)
        post=self.get_object()
        comment.blog=post
        comment.save()
        return super(BlogDetailView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                parent_obj = None
                try:
                    parent_id = int(request.POST.get('parent_id'))
                except:
                    parent_id = None
                if parent_id:
                    parent_obj = Comment.objects.get(id=parent_id)
                    if parent_obj:
                        replay_comment =form.save(commit=False)
                        replay_comment.parent = parent_obj
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    




class BlogView(ListView):
    model = Post
    template_name = 'blog-list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = Post.objects.all().filter(is_published=True)
        context['tag_list'] = Tag.objects.all()
        context['comment_list'] = Comment.objects.all()
        context['category_list'] = Category.objects.all()
        context['count'] = Post.objects.filter(~Q(category=0)).count()
        context['recent'] = Post.objects.all().order_by('created_at')[:4]
        context['filter']=PostFilter(self.request.GET, queryset=self.get_queryset())
        paginator = Paginator(PostFilter(self.request.GET, queryset=self.get_queryset()).qs, 4) 

        
        try:
          page_number = self.request.GET['page']
        except:
            page_number=1
            
        context['page_obj']=paginator.get_page(page_number)
        return context







