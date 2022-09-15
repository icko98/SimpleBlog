from django.contrib import admin
from django.urls import path
from . import views

app_name='website'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('post/<int:post>/', views.post_single, name='post_single'),
    path('post/<int:post>/edit/', views.editpost, name='post_single_edit'),
    path('newpost/', views.newpost, name='new_post'),
    path('author/<str:author>/', views.author_blog, name='author_blog'),
    
]
