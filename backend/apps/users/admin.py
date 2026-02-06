from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Esto añade el campo 'role' al formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Rol', {'fields': ('role',)}),
    )
    # Esto añade la columna 'role' a la lista de usuarios
    list_display = ['username', 'email', 'role', 'is_staff']
    list_filter = ['role', 'is_staff']
