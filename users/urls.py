from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('LoginView',  auth_views.LoginView.as_view(), name='login'),
    path('SignUpView', SignUpView.as_view(), name='signup'),
    path('LogoutView', auth_views.LogoutView.as_view(), name='logout'),
]
