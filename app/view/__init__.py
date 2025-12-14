from .admin_views import *
from .teacher_views import *
from .student_views import *
from .auth_views import *

__all__ = [
    # Admin
    'admin_dashboard',
    'admin_dashboard_class',
    'admin_manage_class',
    'admin_add_group_schedule',
    'admin_add_group',
    'admin_add_room',
    'admin_add_teacher',
    'admin_dashboard_teacher',
    'admin_dashboard_student',
    'admin_add_student',
    'admin_dashboard_report',
    'admin_dashboard_schedule',
    # Teacher
    'teacher_dashboard',
    'teacher_dashboard_schedule',
    'teacher_dashboard_attendance',
    'teacher_dashboard_exam',
    'teacher_dashboard_report',
    'teacher_dashboard_inbox',
    # Student
    'student_dashboard',
    'student_dashboard_schedule',
    'student_dashboard_assignment',
    'student_dashboard_grade',
    'student_dashboard_library',
    'student_dashboard_inbox',
    # Auth
    'login',
    'logout',
]
