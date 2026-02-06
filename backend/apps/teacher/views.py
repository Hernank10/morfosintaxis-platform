from django.shortcuts import render
from apps.users.decorators import teacher_required
from courses.models import Course
from apps.progress.models import LessonProgress

@teacher_required
def dashboard_home(request):
    # Cursos creados por este profesor
    mis_cursos = Course.objects.filter(teacher=request.user)
    
    # Alumnos inscritos en sus cursos (ejemplo simplificado)
    total_alumnos = LessonProgress.objects.filter(lesson__course__teacher=request.user).values('user').distinct().count()

    context = {
        'cursos': mis_cursos,
        'total_alumnos': total_alumnos,
    }
    return render(request, 'teacher/dashboard.html', context)
