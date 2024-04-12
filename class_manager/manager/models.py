from django.db import models

# Create your models here.

class Course(models.Model):
    # PK id created by default id (bigint), you may override that with th e
    # following line
    # id = models.SmallIntegerField(auto_increment=True, primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    teacher = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name

class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    osis = models.IntegerField(max_length=9, unique=True)
    course = models.ManyToManyField(Course)
    grade = models.SmallIntegerField(max_length=12, unique=True)
    gpa = models.FloatField()

    class Meta:
        ordering = ['name']