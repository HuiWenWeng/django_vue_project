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
    path("course/delete/<int:pk>", views.CourseDeleteView.as_view(), name="course_delete"),
    path("student/delete/<int:pk>", views.StudentDeleteView.as_view(), name="student_delete"),
    path("course/update/<int:pk>", views.CourseUpdateView.as_view(), name="course_update"),
    path("student/update/<int:pk>", views.StudentUpdateView.as_view(), name="student_update"),
    path("student/update_bis/<int:pk>", views.StudentUpdatebisView.as_view(), name="student_update_bis",
),
]
