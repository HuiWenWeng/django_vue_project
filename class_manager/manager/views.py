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

from .forms import CourseForm, StudentForm

# Create your views here.

### Course ###
class CourseListView(LoginRequiredMixin, ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Course "{course_name}" has been created'.format(
                course_name=self.object.name))
        return response
    def get_success_url(self):
        return reverse_lazy("manager:course_detail", args=[self.object.id])
        
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("manager:course_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Course "{course_name}" has been deleted'.format(
                course_name=self.object.name))
        return response

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Course "{course_name}" has been updated'.format(
                course_name=self.object.name))
        return response
    
    def get_success_url(self):
        return reverse_lazy("manager:course_detail", args=[self.object.id])

### Student
class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student
    

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Student "{student_name}" has been created'.format(
                student_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("manager:student_detail", args=[self.object.id])
 
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("manager:student_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Student "{student_name}" has been deleted'.format(
                student_name=self.object.name))
        return response
 

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Course "{student_name}" has been updated'.format(
                student_name=self.object.name))
        return response
    
    def get_success_url(self):
        return reverse_lazy("manager:student_detail", args=[self.object.id])