from django.urls import path

from . import views

app_name = "manager"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course_list"),
    path("students", views.StudentListView.as_view(), name="student_list"),
    path("course/<int:pk>", views.CourseDetailView.as_view(), name="course_detail"),
    path("student/<int:pk>", views.StudentDetailView.as_view(), name="student_detail"),
]
