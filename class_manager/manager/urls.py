from django.urls import path

from . import views

app_name = "manager"

urlpatterns = [
    path("course/", views.CourseListView.as_view(), name="course_list"),
    path("student/create", views.StudentCreateView.as_view(), name="student_create"),
    path("course/create", views.CourseCreateView.as_view(), name="course_create")
]
