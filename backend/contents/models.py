from django.db import models
from apps.lessons.models import Lesson

class Content(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='contents', null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    content_type = models.CharField(max_length=50, choices=[('Video', 'Video'), ('Lectura', 'Lectura'), ('PDF', 'PDF')], default='Lectura')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.content_type})"
