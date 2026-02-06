from django.contrib import admin
from .models import LinguisticArea, Exercise

@admin.register(LinguisticArea)
class LinguisticAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('question', 'area', 'level')
    list_filter = ('area', 'level')
