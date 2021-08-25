from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import  password_validation
from django import forms
# from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
# from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
# User = get_user_model()





class User(AbstractUser):
    email = models.EmailField(_('email'), unique=True,)
    image=models.ImageField(null=True,blank=True,max_length=500,upload_to='user_images')
    bio = models.TextField(max_length=500, blank=True,null=True)
    phone = models.CharField(max_length=50, null=True,blank=True)
    address = models.CharField(max_length=50, null=True,blank=True)
    address2=models.CharField(max_length=50, null=True,blank=True)
    country= models.CharField(max_length=50, null=True,blank=True)
    city= models.CharField(max_length=50, null=True,blank=True)





class Checkout(models.Model):
    """
    this model saves checkout information

    """
    #BILLING DETAILS
    user=models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name="checkouts")
    company= models.CharField('company name', max_length=255)
    address=models.CharField('address', max_length=255)
    city=models.CharField('city/town', max_length=100)
    country=models.CharField('country', max_length=100)
    email=models.EmailField('email', max_length=100)
    phone=models.CharField('phone', max_length=13)
    ship_different_address=models.BooleanField(default=False)


    #SHIPPING INFO
    shipping_company= models.CharField('company name', max_length=255)
    shipping_address=models.CharField('address', max_length=255)
    shipping_city=models.CharField('city/town', max_length=100)
    shipping_country=models.CharField('country', max_length=100)
    shipping_email=models.EmailField('email', max_length=100)
    shipping_phone=models.CharField('phone', max_length=13)


    # moderation's
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'


    def __str__(self):
        return self.user.username
        