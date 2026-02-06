from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from morfo_accounts.decorators import teacher_required


@login_required
@teacher_required
def create_course(request):
    return render(request, "courses/create_course.html")
