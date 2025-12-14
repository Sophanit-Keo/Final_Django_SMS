from django.shortcuts import render
import datetime
from app.models import *

# ========================= Student Dashboard =========================
def student_dashboard(request):
    context = {
        "current_date": datetime.date.today(),
    }
    return render(request, 'student/index.html', context)


def student_dashboard_schedule(request):
    return render(request, 'student/schedule.html', {})


def student_dashboard_assignment(request):
    return render(request, 'student/assignment.html', {})


def student_dashboard_grade(request):
    return render(request, 'student/grade.html', {})


def student_dashboard_library(request):
    return render(request, 'student/library.html', {})


def student_dashboard_inbox(request):
    return render(request, 'student/inbox.html', {})
