from django.contrib import admin
from .models import Course, Subject, Lesson, Evaluation

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'is_active')
    inlines = [SubjectInline]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'course') # Cambié 'title' por 'name' porque así está en tu modelo
    list_filter = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'order')
    list_editable = ('order',) # Esto te permite cambiar el orden desde la lista

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'passing_score') # Quité 'max_score' porque no existe en tu modelo
