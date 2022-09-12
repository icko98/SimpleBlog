from django.contrib import admin

# Register your models here.

from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish')

admin.site.register(models.Post, AuthorAdmin )