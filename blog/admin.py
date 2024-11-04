from django.contrib import admin
from django.utils.html import format_html

from blog.models import Category, Post, Contact


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date', 'thumbnail')
    list_filter = ('status', 'created_date', 'published_date', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "-"

    thumbnail.short_description = 'Image'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content', 'created_at']
    list_filter = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'content')
    date_hierarchy = 'created_at'
