from django.db import models


# Create your models here.
class TodoManager(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

