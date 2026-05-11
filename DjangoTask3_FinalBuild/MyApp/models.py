from django.db import models

# Create your models here.
class teacher(models.Model): 
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class school(models.Model): 
    School_Name = models.CharField(max_length=25)
    Location = models.CharField(max_length=30)

class course(models.Model): 
    Course = models.CharField(max_length=25)
    Scalinig = models.CharField(max_length=30)
    Teachers = models.CharField(max_length=30)

class subjects(models.Model): 
    Subjects = models.CharField(max_length=25)