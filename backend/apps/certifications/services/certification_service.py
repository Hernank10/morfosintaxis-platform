from django.db import transaction
from apps.certifications.models import Certification


@transaction.atomic
def issue_global_certificate(student, level):
    """
    Emite un certificado global por nivel.
    Es idempotente: si ya existe, no duplica.
    """

    # Normalizamos nivel
    level = level.upper()

    # Verificar si ya existe
    certificate, created = Certification.objects.get_or_create(
        student=student,
        level=level,
        is_global=True,
    )

    if created:
        # Aquí luego puedes:
        # - enviar email
        # - generar PDF
        # - emitir evento
        print(f"🎓 Certificado GLOBAL emitido: {student} — {level}")
    else:
        print(f"ℹ️ Certificado ya existía: {student} — {level}")

    return certificate
