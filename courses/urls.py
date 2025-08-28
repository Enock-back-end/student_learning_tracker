from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="courses"),
    path("my/", views.my_courses, name="my_courses"),
    path("update/<int:enrollment_id>/", views.update_progress, name="update_progress"),
]
