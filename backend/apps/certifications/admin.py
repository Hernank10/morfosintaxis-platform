from django.contrib import admin
from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("student", "level", "is_global", "issued_at")
    list_filter = ("level", "is_global")
    search_fields = ("student__username",)
