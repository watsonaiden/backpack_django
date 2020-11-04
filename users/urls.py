from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from .views import SignUpView, Login_auth, ChangePassView

urlpatterns = [
    path('login', Login_auth, name='login_auth'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('changepass', ChangePassView.as_view(), name='password_change'),
]
