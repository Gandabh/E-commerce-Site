from django.shortcuts import render
from product.models import *
from django.db.models import Count, Q
from product.forms import ReviewForm
from account.models import User
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from.filters import ProductFilter
from django.core.paginator import Paginator

@register.filter
def get_range(value):
    return range(value)




class ProductView(ListView):
    
    queryset=Product.objects.all().filter(is_published=True)
    template_name='product-list.html'
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list']=Product.objects.all()
        context['image_list']=Image.objects.all()
        context['tag_list']=Tag.objects.all()
        context['category_list']=Category.objects.all()
        context['brands']=Brand.objects.all().filter(is_published=True)
        context['colors']=Color.objects.all()
        context['filter']=ProductFilter(self.request.GET, queryset=self.get_queryset())
        paginator = Paginator(ProductFilter(self.request.GET, queryset=self.get_queryset()).qs, 6) 

        
        try:
          page_number = self.request.GET['page']
        except:
            page_number=1
        context['page_obj']=paginator.get_page(page_number)
        return context
    







class ProductDetailView(FormMixin,DetailView):
    model = Product
    template_name = 'product-detail.html'
    form_class = ReviewForm 
    
    def get_success_url(self):
        return reverse_lazy('product:product_detail', kwargs={'pk': self.object.pk})


    def form_valid(self, form):
            form.instance.user = self.request.user
            review=form.save(commit=False)
            product=self.get_object()
            review.product=product
            review.save()
            return super(ProductDetailView, self).form_valid(form)


    def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
              return self.form_valid(form)
            else:
              return self.form_invalid(form)
    

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['product_list'] = Product.objects.all()
        context['review'] = Review.objects.all()
        context['color'] = Color.objects.all()
        context['image'] = Image.objects.all()
        context['category_list']=Category.objects.all()
        context['filter']=ProductFilter(self.request.GET, queryset=Product.objects.all().filter(is_published=True))
        return context

 



@login_required
def shopping_cart(request):

    context={
        'category_list':Category.objects.all()
    }
    return render(request, 'shopping-cart.html',context)



@login_required
def wishlist(request):

    context={
        'category_list':Category.objects.all()
    }
    
    return render(request, 'wishlist.html',context)






