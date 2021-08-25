from django.contrib import admin

# Register your models here.

from core.models import Subscriber, Contact, Address

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','is_active','created_at','updated_at')  
    list_filter = ('email','is_active')
    search_fields = ('email','is_active')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number','subject','message','created_at','updated_at')  
    list_filter = ('full_name','phone_number','subject','message','created_at','updated_at')  
    search_fields = ('full_name','phone_number','subject','message','created_at','updated_at')  


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address','email','phone')  
    list_filter =  ('address','email','phone')  
    search_fields = ('address','email','phone')  