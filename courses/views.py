from django.shortcuts import render, redirect
from .models import Course
from enrollments.models import Enrollment
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})

@login_required
def enroll_course(request, course_id):
    course = Course.objects.get(id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect("course_list")
