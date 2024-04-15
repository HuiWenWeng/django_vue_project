from django import forms

from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'grade', 'students']
        widgets = {
        }
        
from .models import Student
  
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'osis', 'grade', 'gpa']
        widgets = {
        }