from django.urls import path

from . import views

app_name = "manager"

urlpatterns = [
    path("course/", views.CourseListView.as_view(), name="course_list"),
]
