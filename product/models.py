from django.db import models
from django.http import request
from account.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy



class Brand(models.Model):
    """
    this model saves brands of products
    """
    title = models.CharField('title', max_length=40)


    # moderation's
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Brand'
            verbose_name_plural = 'Brands'


    def __str__(self):
        return self.title



class Tag(models.Model):
    """
    this model saves tags
    """
    name = models.CharField('title', max_length=50)
    # moderation's
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Tag'
            verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name



class Color(models.Model):
    """
    this model saves Colors of products
    """

    title= models.CharField('title',max_length=40)
    

    # moderation's
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Color'
            verbose_name_plural = 'Colors'


    def __str__(self):
        return self.title



class Category(models.Model):
    """
    this model saves Categories
    For example: chair, bag, shoes, table and so on.

    """
    
    title = models.CharField('Basliq', max_length=40)
    

    # moderation's
    is_published = models.BooleanField(default=False)


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title





class Product(models.Model):
    """
    this model saves story products

    """
    title = models.CharField('title', max_length=40)
    description = models.TextField('desc', null=True, blank=True)
    count=models.IntegerField('count', null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,
                                 db_index=True, related_name='products')
    information=models.TextField('info', null=True, blank=True)
    price=models.IntegerField('Price')
    designer=models.CharField('designer', max_length=50)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE,
                                 db_index=True, related_name='products')
    tag=models.ManyToManyField(Tag)
    color=models.ManyToManyField(Color)
    cover_image= models.ImageField('image',upload_to='product_images')
    slide_image= models.ImageField('slide image',upload_to='product_images',null=True,blank=True)
    slogan1 = models.CharField('slogan part 1', max_length=40,null=True,blank=True)
    slogan2 = models.CharField('slogan part 1', max_length=40,null=True,blank=True)
    discount=models.IntegerField('Discount',null=True,blank=True)
    
   


    # moderation's
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def total_price(self):
        if self.discount:
            self.total_price=self.price-(self.price*self.discount)//100
        else:
             self.total_price=self.price
        return self.total_price


    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse_lazy('product:product_detail', kwargs={
            'pk': self.pk
        })

    def get_avg_rating(self):
        reviews = Review.objects.filter(product=self)
        count = len(reviews)
        sum = 0
        for rvw in reviews:
            sum += rvw.rate
        if count==0:
            total=0
        else:
            total=sum/count
        return total




class Review(models.Model):
    """
    this model saves product reviews

    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name="reviews")
    content=models.TextField('Mezmun')
    rate=models.IntegerField(default=1)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,
                                 db_index=True, related_name='reviews')
    

    # moderation's
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username







class Image(models.Model):
    """
    this model saves images of products
    """

    title= models.ImageField('title',upload_to='productdetail_images')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,
                                 db_index=True, related_name='images')
    

    # moderation's
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Image'
            verbose_name_plural = 'Images'


  
class CartItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name="cartItems")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name="cartItems")
    quantity = models.IntegerField(default=1)
    color=models.CharField('color',max_length=255,null=True)

    class Meta:
            verbose_name = 'CartItems'
            verbose_name_plural = 'CartItems'




class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Wishlist'
            verbose_name_plural = 'Wishlist'



