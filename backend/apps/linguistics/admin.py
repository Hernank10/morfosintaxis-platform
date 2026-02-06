from django.contrib import admin
from .models import LinguisticArea, Exercise

@admin.register(LinguisticArea)
class LinguisticAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    # Estos campos deben existir en el modelo de arriba
    list_display = ('title', 'area')
    list_filter = ('area',)
