from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment

def course_list(request):
    return render(request, "courses/list.html", {"courses": Course.objects.all()})

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, "courses/my_courses.html", {"enrollments": enrollments})

@login_required
def update_progress(request, enrollment_id):
    enroll = get_object_or_404(Enrollment, id=enrollment_id, user=request.user)
    if enroll.progress < 100:
        enroll.progress = min(100, enroll.progress + 50)
        enroll.save()
    return redirect("my_courses")
