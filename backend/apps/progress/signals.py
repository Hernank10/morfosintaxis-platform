from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.progress.models import LevelProgress
from apps.certifications.services.certification_service import (
    issue_global_certificate
)


@receiver(post_save, sender=LevelProgress)
def issue_certificate_on_level_completion(sender, instance, created, **kwargs):
    """
    Emite certificado GLOBAL automáticamente
    cuando el estudiante completa un nivel CEFR.
    """

    if not instance.is_completed:
        return

    issue_global_certificate(
        student=instance.student,
        level=instance.level
    )
