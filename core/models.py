from django.db import models
from django.db.models.aggregates import Max
from account.models import User


class Subscriber(models.Model):
    """
    this model saves subscribers
    """

    email=models.EmailField("Email",max_length=40,unique=True)

    # moderation's
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email





class Contact(models.Model):

    full_name=models.CharField("Adinizi ve Soyadinizi daxil edin",max_length=100)
    email=models.EmailField("Emailinizi daxil edin",max_length=30)
    phone_number=models.CharField("Mobil nomreniz",max_length=13)
    subject=models.CharField("Movzu",max_length=30)
    message=models.TextField("Metn")

    # moderation's
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name



class Address(models.Model):
    """
    this model saves PAVSHOP addresses and 

    """

    address=models.TextField('address')
    email=models.EmailField("Email",max_length=50)
    phone=models.CharField("Phone number",max_length=13)



    # moderation's
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


