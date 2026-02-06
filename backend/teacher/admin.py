from django.contrib import admin
from .models import TeacherProfile

@admin.register(TeacherProfile)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
