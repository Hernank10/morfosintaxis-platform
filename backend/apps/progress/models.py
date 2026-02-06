from django.db import models  # <--- ESTA ES LA LÍNEA QUE FALTA
from django.contrib.auth import get_user_model

User = get_user_model()

# 🎓 Niveles CEFR oficiales
CEFR_LEVELS = [
    ("A1", "A1 – Acceso"),
    ("A2", "A2 – Plataforma"),
    ("B1", "B1 – Umbral"),
    ("B2", "B2 – Avanzado"),
    ("C1", "C1 – Dominio operativo"),
    ("C2", "C2 – Maestría"),
]


class LevelProgress(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="level_progress"
    )

    level = models.CharField(
        max_length=2,
        choices=CEFR_LEVELS
    )

    mastery = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Regla académica: 100% = nivel completado
        if self.mastery >= 100:
            self.is_completed = True

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("student", "level")
        ordering = ["level"]

    def __str__(self):
        status = "✔" if self.is_completed else "⏳"
        return f"{self.student} — {self.level} {status}"


from django.db import models
from django.conf import settings

class LessonProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE  # <--- Debe decir 'on_delete'

    )
    # Por ahora comentamos la lección si aún no has definido el modelo Lesson
    # lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Lesson Progresses"
