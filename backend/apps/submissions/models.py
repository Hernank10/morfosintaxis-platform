from django.db import models
from django.conf import settings
from apps.linguistics.models import Exercise

class Submission(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='submissions'
    )
    exercise = models.ForeignKey(
        Exercise, 
        on_delete=models.CASCADE, 
        related_name='student_submissions'
    )
    answer_text = models.TextField(verbose_name="Respuesta del Alumno")
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    # Campos para la corrección
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Nota")
    teacher_feedback = models.TextField(blank=True, verbose_name="Retroalimentación")
    is_reviewed = models.BooleanField(default=False, verbose_name="Revisado")

    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"

    def __str__(self):
        return f"{self.student.username} - {self.exercise.title}"
