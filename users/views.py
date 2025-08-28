from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from courses.models import Course, Enrollment


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. You can now log in.")
            return redirect("login")
        # form invalid -> fall through and render with errors
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        return render(request, "users/login.html", {"error": "Invalid username or password"})
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard_view(request):
    courses = Course.objects.all()
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, "users/dashboard.html", {"courses": courses, "enrollments": enrollments})

@login_required
def enroll_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect("dashboard")