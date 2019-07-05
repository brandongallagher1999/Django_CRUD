from django.db import models

# Create your models here.

class Work_Order(models.Model):
    title = models.TextField()
    desc = models.TextField()
    deadline = models.TextField()