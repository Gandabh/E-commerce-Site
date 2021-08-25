from django import forms
from account.models import Checkout
from django.forms import ModelForm
from django.contrib.auth import  get_user_model,password_validation
from django.contrib import messages
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    UserCreationForm, UsernameField, AuthenticationForm, PasswordResetForm, SetPasswordForm,PasswordChangeForm
)

User = get_user_model()


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email', 
            'password1',
            'password2', 
            'phone',
            'address',
            'country',
            'city', 
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
        
        }


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Confirm password is not same with password')
        return password2

    def _post_clean(self):
        super()._post_clean()
        password1 = self.cleaned_data.get('password1')
        # print('here', self.instance.username)
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1





class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                           'class': 'form-control',
                                                           'placeholder': 'Username'
                                                           }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }),
    )




class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), max_length=255)


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        }),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        }),
    )


class CustomChangePasswordForm(PasswordChangeForm):

    old_password=forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder': 'Old Password',
            'type':'password'
            })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password',
            'type':'password'
        }),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password',
            'type':'password'
        }),
    )



class CheckoutForm(ModelForm):

    company=forms.CharField(max_length=255,label='COMPANY NAME',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    address=forms.CharField(max_length=255,required=True,label='*ADDRESS',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    city=forms.CharField(max_length=255,required=True,label='*TOWN/CITY',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    country=forms.CharField(max_length=255,label='COUNTRY',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    email= forms.EmailField(max_length=50,required=True,label='*EMAIL ADDRESS',widget=forms.EmailInput(attrs={'class': 'col-md-6',}))
    phone= forms.CharField(max_length=13,required=True,label='*PHONE',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    

    shipping_company=forms.CharField(max_length=255,label='COMPANY NAME',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    shipping_address=forms.CharField(max_length=255,required=True,label='*ADDRESS',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    shipping_city=forms.CharField(max_length=255,required=True,label='*TOWN/CITY',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    shipping_country=forms.CharField(max_length=255,label='COUNTRY',widget=forms.TextInput(attrs={'class': 'col-md-6',}))
    shipping_email= forms.EmailField(max_length=50,required=True,label='*EMAIL ADDRESS',widget=forms.EmailInput(attrs={'class': 'col-md-6',}))
    shipping_phone= forms.CharField(max_length=13,required=True,label='*PHONE',widget=forms.TextInput(attrs={'class': 'col-md-6',}))


    class Meta:
            model = Checkout
            fields=(
        'company',
        'address',
        'city',
        'country',
        'email',
        'email', 
        'phone', 

        'shipping_company',
        'shipping_address',
        'shipping_city',
        'shipping_country',
        'shipping_email',
        'shipping_email', 
        'shipping_phone', 


        )