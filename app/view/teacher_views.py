from django.shortcuts import render
from app.models import *

# ========================= Teacher Dashboard =========================
def teacher_dashboard(request):
    return render(request, 'teacher/index.html', {})


def teacher_dashboard_schedule(request):
    return render(request, 'teacher/schedule.html', {})


def teacher_dashboard_attendance(request):
    return render(request, 'teacher/attendance.html', {})


def teacher_dashboard_exam(request):
    return render(request, 'teacher/exam.html', {})


def teacher_dashboard_report(request):
    return render(request, 'teacher/report.html', {})


def teacher_dashboard_inbox(request):
    return render(request, 'teacher/inbox.html', {})
