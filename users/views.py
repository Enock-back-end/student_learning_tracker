# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the authenticated user
            login(request, user)
            return redirect("home") # Or "dashboard", depending on your URL
        else:
            # Render login page with an error message
            return render(request, "login.html", {"error": "Invalid username or password"})
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
# Dashboard view
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "dashboard.html")
