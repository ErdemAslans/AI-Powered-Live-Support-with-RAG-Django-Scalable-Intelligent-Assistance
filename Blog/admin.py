from django.contrib import admin
from .models import BlogModel

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'is_active', 'created_at', 'updated_at')
admin.site.register(BlogModel, BlogAdmin)