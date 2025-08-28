from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("users/", include("users.urls")),
    path("courses/", include("courses.urls")),
    path('assignments/', include('assignments.urls')),
]

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "users/dashboard.html") 