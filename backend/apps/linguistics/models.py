from django.db import models

class LinguisticArea(models.Model):
    name = models.CharField(max_length=100, verbose_name="Área Lingüística")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    # Estos nombres deben coincidir EXACTAMENTE con el admin.py
    area = models.ForeignKey(LinguisticArea, on_delete=models.CASCADE, related_name='exercises')
    title = models.CharField(max_length=200, verbose_name="Título")
    instructions = models.TextField()
    example_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.area.name} - {self.title}"
