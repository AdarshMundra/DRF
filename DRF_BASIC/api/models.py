from django.db import models

# Create your models here.

class Stundet(models.Model):
    stuName = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)