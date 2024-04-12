from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.base import TemplateView

from .models import Course, Student
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

# Create your views here.

### Course ###
class CourseListView(LoginRequiredMixin, ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
    
### Student ### 
class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student