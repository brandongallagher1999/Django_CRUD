from django.db import models

# Create your models here.


class Worker(models.Model):
    name = models.TextField()
    company_name = models.TextField()
    email = models.TextField()

