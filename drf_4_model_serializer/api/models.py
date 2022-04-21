import email
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    roll=models.IntegerField()
    email=models.EmailField(blank=True)