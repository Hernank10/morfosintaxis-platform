from django.shortcuts import render
from apps.users.decorators import teacher_required
from courses.models import Course

@teacher_required
def dashboard(request):
    courses = Course.objects.filter(teacher=request.user)

    return render(request, "teacher/dashboard.html", {
        "courses": courses
    })

