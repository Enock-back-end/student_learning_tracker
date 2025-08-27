# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

     
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already taken"})
        else:
        
            user = User.objects.create_user(username=username, password=password)
            # Log in the user automatically after signup
            login(request, user)
            return redirect("home")
    
    return render(request, "signup.html")

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