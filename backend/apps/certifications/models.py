from django.db import models
from apps.courses.models import Course
from django.conf import settings


class Certification(models.Model):
    LEVEL_CHOICES = [
        ("A1", "A1"),
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="certifications"
    )

    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES
    )

    # True → certificado global (todas las skills)
    # False → certificado por skill (futuro)
    is_global = models.BooleanField(default=True)

    issued_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "level", "is_global")
        ordering = ["-issued_at"]

    def __str__(self):
        scope = "Global" if self.is_global else "Skill"
        return f"{self.student} — {scope} {self.level}"
