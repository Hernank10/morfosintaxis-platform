from django.conf import settings
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "teacher"},
        related_name="courses_taught" # Cambié esto para evitar conflictos
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.course.title})"

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Evaluation(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='evaluations')
    title = models.CharField(max_length=200)
    passing_score = models.IntegerField(default=60)

    def __str__(self):
        return self.title


