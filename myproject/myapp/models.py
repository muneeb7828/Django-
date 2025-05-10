from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Contact(models.Model):
    name= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()


    