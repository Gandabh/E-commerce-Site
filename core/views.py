from django.db.models.aggregates import Count
from django.shortcuts import redirect, render
from django.db.models import Count, Q
from product.models import *
from blog.models import *
from core.forms import ContactForm
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
import product
import blog
from product.filters import ProductFilter
from django.contrib import messages
from core.models import Address





class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm   
    success_url = '/'

    def get_success_url(self):
        messages.success(self.request, 'Your message sent successfully!')
        return super(ContactView, self).get_success_url()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list']=Category.objects.all()
        context['filter']=ProductFilter(self.request.GET, queryset=Product.objects.all().filter(is_published=True))

        return context




class AboutView(ListView):
    queryset=Product.objects.all().filter(is_published=True)
    template_name = 'about-us.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list']=Category.objects.all()
        context['filter']=ProductFilter(self.request.GET, queryset=Product.objects.all().filter(is_published=True))

        return context




class IndexView(ListView):
    
    queryset=Product.objects.all().filter(is_published=True)
    template_name='index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter']=ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['products']=Product.objects.all()
        context['recents']=Product.objects.all().order_by('created_at')[:8]
        context['category_list']=Category.objects.all()

        return context


    


def reviews(request):

    #last three blog posts
    print('last three blog posts: ',Post.objects.all()[:3][::-1])
    print("=================")

    #ordering by prices and created dates of products
    print('ordering by prices and created dates of products: ',Product.objects.order_by('price','created_at'))
    print("=================")

    #category of products
    product=Product.objects.all()
    for p in product:
        print('category of products: ',p.category)


    #function that returns reviews about a product inserted in the search field
    search = request.GET.get('search')
    print('searched value', search)
    review = Post.objects.all()
    if search:
        review = Review.objects.filter(Q(product__title__icontains=search))

    context = {
        'review_list': review,
    }
    return render(request, 'reviews-list.html', context)


#function that returns comments about a blog post inserted in the search field
def comments(request):
    search = request.GET.get('search')
    print('searched value', search)
    comment = Comment.objects.all()
    if search:
       comment=Comment.objects.filter(Q(blog__title__icontains=search))

    context = {
        'comment_list': comment,
    }
    return render(request, 'comment-list.html', context)


# def blog_post(request):
#     search=request.GET.get('search')
#     posts=Post.objects.all()
#     c_list=[]
#     for p in posts:
#         c_list.append(p.category.title)
#     print('Blogun kateqoriyalari:',c_list)
#     if search:
#         posts=posts.filter(Q(title__startswith=search) | Q(category__title__startswith=search))
#     context={
#         'post_list':posts
#     }
#     tags=Tag.objects.all()[:5]
#     print(tags)
#     return render(request,'blog-post.html',context)





# def product_search(request):
#     search = request.GET.get('search')
#     print('searched value', search)
#     product = Product.objects.all()
#     if search:
#         product = Product.objects.all().filter(Q(title__icontains=search))

#     context = {
#         'product_list': product,
#     }



#     return render(request, 'product-search.html', context)


def product_search(request):
    search = request.GET.get('search')
    print('searched value', search)
    
    product1 = Product.objects.all()
    if search:
        product1 = product1.filter(Q(title__icontains=search))


    context = {
        'product_list': product1,
    }

    print('Most popular 5 product tags',product.models.Tag.objects.annotate(num_rev=Count('product'))[:5])


    product_ls=Product.objects.all()
    if search:
        product_tag=Product.objects.all().filter(Q(title__icontains=search)).first().tag.all()
        for i in product_tag:
            print('tag ',i)
            product_ls=Product.objects.all().filter(Q(tag=i))[:8]

    return render(request, 'product-search.html', context)



def blog_post(request):
    search=request.GET.get('search')
    posts=Post.objects.all()
    c_list=[]
    for p in posts:
        c_list.append(p.category.title)
    print('Blogun kateqoriyalari:',c_list)
    if search:
        posts=posts.filter(Q(title__startswith=search) | Q(category__title__startswith=search))
    context={
        'post_list':posts
    }
    print('Most popular 5 post tags',blog.models.Tag.objects.annotate(num_rev=Count('post'))[:5]) 

    blog_list=Post.objects.all()
    if search:
        blog_tag=Post.objects.all().filter(Q(title__icontains=search)).first().tag.all()
        for i in blog_tag:
            print('tag ',i)
            blog_list=Post.objects.all().filter(Q(tag=i))[:3]

    return render(request,'blog-post.html',context)