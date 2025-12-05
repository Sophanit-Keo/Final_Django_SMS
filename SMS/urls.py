"""
URL configuration for SMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    # Admin site
    path('supper-admin/', admin.site.urls),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-classes/', admin_dashboard_class, name='admin_dashboard_classes'),
    path('admin-teacher/', admin_dashboard_teacher, name='admin_dashboard_teacher'),
    path('admin-student/', admin_dashboard_student, name='admin_dashboard_student'),
    path('admin-report/', admin_dashboard_report, name='admin_dashboard_report'),
    path('admin-schedule/', admin_dashboard_schedule, name='admin_dashboard_schedule'),
        # Class Admin
    path('admin-add-class/', admin_manage_class, name='admin_manage_class'),
    path('admin-add-group/', admin_add_group_schedule, name='admin_add_group_schedule'),
    path('admin-add-group-schedule/', admin_add_group, name='admin_add_group'),
    path('admin-add-room/', admin_add_room, name='admin_add_room'),
        # Student Admin
    path('admin-add-student/', admin_add_student, name='admin_add_student'),
        # Teacher Admin
    path('admin-add-teacher/', admin_add_teacher, name='admin_add_teacher'),
    # Teacher Dashboard
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher-schedule/', teacher_dashboard_schedule, name='teacher_dashboard_schedule'),
    path('teacher-attendance/', teacher_dashboard_attendance, name='teacher_dashboard_attendance'),
    path('teacher-inbox/', teacher_dashboard_inbox, name='teacher_dashboard_inbox'),
    path('teacher-report/', teacher_dashboard_report, name='teacher_dashboard_report'),
    path('teacher-exam/', teacher_dashboard_exam, name='teacher_dashboard_exam'),
    # Student Dashboard
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('student-schedule/', student_dashboard_schedule, name='student_dashboard_schedule'),
    path('student-assignment/', student_dashboard_assignment, name='student_dashboard_assignment'),
    path('student-grade/', student_dashboard_grade, name='student_dashboard_grade'),
    path('student-library/', student_dashboard_library, name='student_dashboard_library'),
    path('student-inbox/', student_dashboard_inbox, name='student_dashboard_inbox'),
]
