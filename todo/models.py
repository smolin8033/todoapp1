from django.db import models

class TodoItem(models.Model):
    content = models.TextField(max_length=10000)

# Create your models here.
