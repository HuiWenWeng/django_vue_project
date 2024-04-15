from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    osis = models.IntegerField(unique=True)
    grade = models.SmallIntegerField(unique=False)
    gpa = models.FloatField(max_length=10, unique=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name
        
        
class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    teacher = models.CharField(max_length=200, unique=False)
    students = models.ManyToManyField(Student)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name