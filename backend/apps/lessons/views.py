from apps.courses.models import Course
from apps.lessons.models import Lesson
from django.contrib.auth.decorators import login_required
from morfo_accounts.decorators import teacher_required

@login_required
@teacher_required
def create_lesson(request):
    return render(request, "lessons/create_lesson.html")
