from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=20)