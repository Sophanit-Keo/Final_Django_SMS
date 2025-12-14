from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import Student, Teacher

# ========================= Authentication =========================
def login(request):
    """Login view - authenticate user and create session"""
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        try:
            # Get user by email (username field stores email)
            user = User.objects.get(username=email)
            
            # Verify password
            if user.check_password(password):
                # Create session and authenticate
                auth_login(request, user)
                
                # Redirect based on user role
                if user.is_staff:
                    return redirect("admin_dashboard")
                
                # Check if user has Teacher profile
                try:
                    teacher = Teacher.objects.get(user=user)
                    return redirect("teacher_dashboard")
                except Teacher.DoesNotExist:
                    pass
                
                # Check if user has Student profile
                try:
                    student = Student.objects.get(user=user)
                    return redirect("student_dashboard")
                except Student.DoesNotExist:
                    pass
                
                # If no role found, redirect to login with error
                return render(request, "login.html", {"error": "User has no assigned role"})
            else:
                return render(request, "login.html", {"error": "Invalid credentials"})
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid credentials"})
        except Exception as e:
            return render(request, "login.html", {"error": f"Login error: {str(e)}"})

    return render(request, "login.html", {})


@login_required(login_url='login')
def logout(request):
    """Logout user and redirect to login page"""
    auth_logout(request)
    return redirect("login")
