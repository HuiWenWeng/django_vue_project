from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    osis = models.IntegerField(unique=True, default='0000000')
    grade = models.SmallIntegerField(unique=False, default='9')
    gpa = models.FloatField(max_length=10, unique=False, default='100')

    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name
        
        
class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    teacher = models.CharField(max_length=200, unique=False)
    grade = models.SmallIntegerField(unique=False)
    students = models.ManyToManyField(Student)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name