from django.urls import path

from . import views

app_name = "manager"

urlpatterns = [

    path("student/create", views.StudentCreateView.as_view(), name="student_create"),
    path("course/create", views.CourseCreateView.as_view(), name="course_create"),
    path("", views.CourseListView.as_view(), name="course_list"),
    path("students", views.StudentListView.as_view(), name="student_list"),
    path("course/<int:pk>", views.CourseDetailView.as_view(), name="course_detail"),
    path("student/<int:pk>", views.StudentDetailView.as_view(), name="student_detail"),
]
