from django.urls import path
from app.view import (
    admin_dashboard,
    admin_dashboard_class,
    admin_manage_class,
    admin_add_group_schedule,
    admin_add_group,
    admin_add_room,
    admin_dashboard_teacher,
    admin_add_teacher,
    admin_dashboard_student,
    admin_add_student,
    admin_dashboard_report,
    admin_dashboard_schedule,
)

urlpatterns = [
    # Dashboard
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    
    # Classes Management
    path('admin-classes/', admin_dashboard_class, name='admin_dashboard_classes'),
    path('admin-manage-class/', admin_manage_class, name='admin_manage_class'),
    path('admin-add-group/', admin_add_group_schedule, name='admin_add_group_schedule'),
    path('admin-add-group-schedule/', admin_add_group, name='admin_add_group'),
    path('admin-add-room/', admin_add_room, name='admin_add_room'),
    
    # Teachers Management
    path('admin-teacher/', admin_dashboard_teacher, name='admin_dashboard_teacher'),
    path('admin-add-teacher/', admin_add_teacher, name='admin_add_teacher'),
    
    # Students Management
    path('admin-student/', admin_dashboard_student, name='admin_dashboard_student'),
    path('admin-add-student/', admin_add_student, name='admin_add_student'),
    
    # Reports & Schedules
    path('admin-report/', admin_dashboard_report, name='admin_dashboard_report'),
    path('admin-schedule/', admin_dashboard_schedule, name='admin_dashboard_schedule'),
]
