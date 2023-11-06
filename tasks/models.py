from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  titulo = models.CharField(max_length=100)
  descripcion = models.TextField(blank=True)
  created = models.DateTimeField(auto_now_add=True)
  fechaterminada = models.DateTimeField(null=True)
  prioridad = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE) 