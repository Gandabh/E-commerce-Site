from django import forms
from django.db.models import fields
from django.forms import ModelForm
from core.models import Contact


class ContactForm(forms.ModelForm):

    full_name=forms.CharField(label="Name and Surname",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','name':"name", 'id':"name"}))
    email=forms.EmailField(label="Email",max_length=30,widget=forms.EmailInput(attrs={'class':'form-control','name':"email", 'id':"email"}))
    phone_number=forms.CharField(label="Phone",max_length=13,widget=forms.TextInput(attrs={'class':'form-control','name':"company", 'id':"company"}))
    subject=forms.CharField(label="Subject",max_length=30,widget=forms.TextInput(attrs={'class':'form-control','name':"website", 'id':"website"}))
    message=forms.CharField(label="Context",widget=forms.Textarea(attrs={'class':'form-control','name':"message", 'id':"message"}))

    class Meta:
        model=Contact
        fields=['full_name','email','phone_number','subject','message']
    