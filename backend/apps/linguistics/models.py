from django.db import models
from apps.lessons.models import Lesson

class LinguisticArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self): return self.name

class Exercise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='exercises', null=True)
    area = models.ForeignKey(LinguisticArea, on_delete=models.CASCADE)
    question = models.TextField()
    correct_answer = models.TextField(help_text="La respuesta esperada")
    feedback = models.TextField(help_text="Explicación pedagógica")
    level = models.CharField(max_length=50, default='Básico')

    def __str__(self): return f"{self.question[:50]}..."
