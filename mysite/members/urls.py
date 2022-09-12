from django.contrib import admin
from django.urls import path
from . import views

app_name='members'

urlpatterns = [
    path('login_user', views.login_user, name='loginuser'),
    path('logout_user', views.logout_user, name='logoutuser'),
    path('register_user', views.register_user, name='registeruser'),
    
]