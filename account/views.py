from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from account.tasks import send_confirmation_mail
from account.utils.tokens import account_activation_token
from account.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView,PasswordChangeView
from account.forms import RegistrationForm, LoginForm, CustomPasswordResetForm,CheckoutForm, CustomSetPasswordForm,CustomChangePasswordForm
from django.contrib.auth.decorators import login_required
from product.models import Category

User = get_user_model()



class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_reset_email.html'
    form_class = CustomPasswordResetForm
    template_name = 'forget_password.html'
    success_url = reverse_lazy('core:index')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(CustomPasswordResetView, self).get_success_url()




class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed')
        return super(CustomPasswordResetConfirmView, self).get_success_url()



class CustomPasswordChangeView(PasswordChangeView):

    template_name='change_password.html'
    form_class=CustomChangePasswordForm
    success_url=reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed')
        return super(CustomPasswordChangeView, self).get_success_url()



class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('account:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.is_active = False
        result = super().form_valid(form)
        user = form.instance
        send_confirmation_mail(user)
        messages.success(self.request, 'We sent Confirmation Email !')
        return result




class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

   
   

def logout(request):
    django_logout(request)
    return redirect('/')



def activate(request, uidb64, token):
    
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your account activated')
        user.is_active = True
        user.save()
        return redirect('account:login')
    else:
        messages.error(request, 'your link expired or link invalid')
        return redirect('/')



@login_required
def checkout(request):
    form = CheckoutForm()
    

    if request.method == 'POST':
        checkout_data = request.POST
        form = CheckoutForm(data=checkout_data)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('/')
            
    context = {
        'form': form,
        'category_list':Category.objects.all()
       }


    return render(request, 'checkout.html',context)

