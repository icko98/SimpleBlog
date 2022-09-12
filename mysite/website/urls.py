from django.contrib import admin
from django.urls import path
from . import views

app_name='website'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('post/<slug:post>/', views.post_single, name='post_single'),
    path('newpost/', views.newpost, name='new_post'),
    #path('/author/<slug:author>/', views.author_blog, name='author_blog')
    path('author/<str:author>/', views.author_blog, name='author_blog'),
    
]
