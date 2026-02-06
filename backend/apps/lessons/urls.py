from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from morfo_accounts.decorators import teacher_required

path(
    "create/",
    login_required(teacher_required(views.create_lesson)),
    name="lesson_create"
),
