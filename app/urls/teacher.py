from django.urls import path
from app.view import (
    teacher_dashboard,
    teacher_dashboard_schedule,
    teacher_dashboard_attendance,
    teacher_dashboard_inbox,
    teacher_dashboard_report,
    teacher_dashboard_exam,
)

urlpatterns = [
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher-schedule/', teacher_dashboard_schedule, name='teacher_dashboard_schedule'),
    path('teacher-attendance/', teacher_dashboard_attendance, name='teacher_dashboard_attendance'),
    path('teacher-inbox/', teacher_dashboard_inbox, name='teacher_dashboard_inbox'),
    path('teacher-report/', teacher_dashboard_report, name='teacher_dashboard_report'),
    path('teacher-exam/', teacher_dashboard_exam, name='teacher_dashboard_exam'),
]
