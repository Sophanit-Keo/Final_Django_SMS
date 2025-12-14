from django.shortcuts import render, redirect
from app.models import *

# ========================= Authentication =========================
def login(request):
    if request.method == "POST":
        username = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        # Use environment variables or Django settings for credentials
        # TODO: Implement proper authentication system
        ADMIN_EMAIL = "admin@school.edu"
        ADMIN_PASSWORD = "admin123"
        TEACHER_EMAIL = "teacher@school.edu"
        TEACHER_PASSWORD = "teacher123"
        STUDENT_EMAIL = "student@school.edu"
        STUDENT_PASSWORD = "student123"

        if username == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            return redirect("admin_dashboard")
        elif username == TEACHER_EMAIL and password == TEACHER_PASSWORD:
            return redirect("teacher_dashboard")
        elif username == STUDENT_EMAIL and password == STUDENT_PASSWORD:
            return redirect("student_dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html", {})


def logout(request):
    """Logout user and redirect to login page"""
    return redirect("login")
