from django.contrib import admin
from account.models import Checkout
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import User
from django.contrib.auth.admin import UserAdmin



User = get_user_model()
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ( 'email', 'bio', 'image', 'phone','address','address2','country','city')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('user','company','city','country','email','phone')
    list_filter = ('user','company','city','country','email','phone')
    search_fields = ('user','company','city','country','email','phone')
