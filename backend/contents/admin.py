from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'content_type', 'created_at')
    list_filter = ('content_type', 'lesson')
