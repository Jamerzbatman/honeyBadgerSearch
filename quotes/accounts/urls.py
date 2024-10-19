# In views.py of your accounts app
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import custom_login, register

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='sign_in'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='sign_in'),
]
