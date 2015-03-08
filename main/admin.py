# coding=utf-8

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'status', 'start_publication', 'end_publication']
    list_display = ('title', 'slug', 'status',)


class TagAdmin(admin.ModelAdmin):
    fields = ['tag', 'is_deleted']
    list_display = ('tag', 'is_deleted', )


admin.site.register(Post, PostAdmin)