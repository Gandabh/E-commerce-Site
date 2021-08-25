from django.urls import path, re_path, include
from account.views import (
    RegisterView,
    CustomLoginView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    CustomPasswordChangeView,
    logout,
    activate,
    checkout
)

app_name = 'account'
urlpatterns = [
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('reset-password/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='reset-password'),
    path('checkout/',checkout, name='checkout'),
    path('forget-password/', CustomPasswordResetView.as_view(), name='password-reset-view'),
    path('change-password/',CustomPasswordChangeView.as_view(),name='change-password')
]