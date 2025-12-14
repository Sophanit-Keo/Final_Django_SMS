from django.urls import path
from app.view import (
    student_dashboard,
    student_dashboard_schedule,
    student_dashboard_assignment,
    student_dashboard_grade,
    student_dashboard_library,
    student_dashboard_inbox,
)

urlpatterns = [
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('student-schedule/', student_dashboard_schedule, name='student_dashboard_schedule'),
    path('student-assignment/', student_dashboard_assignment, name='student_dashboard_assignment'),
    path('student-grade/', student_dashboard_grade, name='student_dashboard_grade'),
    path('student-library/', student_dashboard_library, name='student_dashboard_library'),
    path('student-inbox/', student_dashboard_inbox, name='student_dashboard_inbox'),
]
