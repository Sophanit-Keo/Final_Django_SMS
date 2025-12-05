from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
import datetime
from app.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
#========================= Admin =========================
def admin_dashboard(request):
    trend_list_enrollment = enrollment_trends()
    student_total = Student.objects.count()
    teacher_total = Teacher.objects.count()
    group_total = Group.objects.count()
    context = {
        "current_date": datetime.date.today(),
        "student_total": student_total,
        "teacher_total": teacher_total,
        "group_total": group_total,
        "trend_list": trend_list_enrollment,
    }
    return render(request, "admin/indexs.html", context)
#--------- admin_class ---------#
def admin_dashboard_class(request):
    groups = Group.objects.all()
    timetable = Timetable.objects.select_related('group_id', 'teacher_id', 'classroom_id').all()
    context = {
        "groups": groups,
        "timetables": timetable,
    }
    return render(request, 'admin/classes/classes.html',context)
#--------- admin_teacher ---------#
def admin_add_teacher(request):
    teachers = Teacher.objects.prefetch_related("subject_set").all()
    subjects = Subject.objects.all()
    teacher = Teacher()
    context = {
        "teachers" : teachers,
        "subjects" : subjects
    }
    if request.method == "POST":
        print("POST is call")
        try:
            teacher.first_name = request.POST.get('first_name')
            teacher.last_name = request.POST.get('last_name')
            teacher.gender = request.POST.get('gender')
            teacher.date_of_birth = request.POST.get('date_of_birth')
            teacher.status = request.POST.get('status')
            teacher.hire_date = request.POST.get('hire_date')
            teacher.phone_number = request.POST.get('phone_number')
            teacher.email = request.POST.get('email')
            teacher.address = request.POST.get('address')
            subject_id = request.POST.get('subject')
            teacher.save()
            teacher.school_email = f'{teacher.first_name}.{teacher.last_name}.{teacher.id}@school.edu.kh'
            teacher.save()
            if subject_id:
                selected_subject = Subject.objects.filter(id=subject_id)
                for subject in selected_subject:
                    subject.teacher_id.add(teacher)

            return redirect("admin_dashboard_teacher")
        except Exception as e:
            context['error'] = f"Error adding teacher: {str(e)}"
            print(context['error'])
            return render(request, 'admin/teacher/add_teacher.html', context)
    return render(request, 'admin/teacher/add_teacher.html',context)

def admin_dashboard_teacher(request):
    teachers = Teacher.objects.prefetch_related("subject_set").all()
    subjects = Subject.objects.prefetch_related("teacher_set").all()
    context = {
        "teachers" : teachers,
        "subjects" : subjects
    }
    if request.method == "POST":
        method = request.POST.get("_method")
        if method =="DELETE":
            teacher_id = request.POST.get("teacher_id")
            Teacher.objects.filter(id = teacher_id).delete()
            return redirect("admin_dashboard_teacher")
    return render(request, 'admin/teacher/teachers.html',context)

#--------- admin_student ---------#
def admin_dashboard_student(request):
    students = Student.objects.prefetch_related('enrollment_set').all()
    context = {
        "current_date": datetime.date.today(),
        "students": students,
    }
    if request.method == "POST":
        method = request.POST.get('_method')
        if method == 'DELETE':
            Student.objects.filter(id =request.POST.get('student_id')).delete()
            print(request.POST.get('student_id'))
            return redirect('admin_dashboard_student')
    return render(request, 'admin/student/students.html',context)
def admin_add_student(request):
    students = Student.objects.all()
    guardians = Guardian.objects.prefetch_related("student_set").all()
    enrollments = Enrollment.objects.select_related("student_id","subject_id","group_id").all()
    groups = Group.objects.all()
    student_id = Student.objects.order_by('-id').values_list('id', flat=True).first()+1
    student = Student()
    guardian = Guardian()
    enrollment = Enrollment()
    
    context = {
        'student_last_id':student_id,
        'students':students,
        'guardians':guardians,
        'enrollments':enrollments,
        'groups':groups
    }
    if request.method == 'POST':
        try:
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.date_of_birth = request.POST.get('date_of_birth')
            student.email = request.POST.get('email')
            student.address = request.POST.get('address')
            student.phone_number = request.POST.get('phone_number')
            student.gender = request.POST.get('gender')
            student.status = request.POST.get('status')
            student.start_date = datetime.date.today()
            student.special_needs = request.POST.get('special_needs')
            student.save()
            student.school_email = f'{student.first_name}.{student.last_name}.{student.id}@school.edu'
            student.save()

            # Add Guardian
            guardian.first_name = request.POST.get('g_first_name')
            guardian.last_name = request.POST.get('g_last_name')
            guardian.phone_number = request.POST.get('g_phone_number')
            guardian.email = request.POST.get('g_email')
            guardian.relationship = request.POST.get('relationship')
            guardian.address = request.POST.get('address')
            guardian.save()

            # Add to Enrollment
            enrollment.enrollment_date = datetime.date.today()
            enrollment.status = request.POST.get('enrollment_status', 'active')
            enrollment.student_id = student
            group_id = request.POST.get('group')
            if group_id:
                enrollment.group_id = Group.objects.get(id=group_id)
            enrollment.save()

            # Relationship Guardian and Student
            guardian.student_id.add(student.id)
            return redirect('admin_dashboard_student')
        except Exception as e:
            context['error'] = f"Error adding teacher: {str(e)}"
            print(context['error'])
            return redirect('admin_add_student')

    return render(request, 'admin/student/add_student.html',context)

def admin_dashboard_report(request):
    return render(request, 'admin/reports.html',{})
def admin_dashboard_schedule(request):
    return render(request, 'admin/schedules.html',{})
    #-------- Class Admin #--------
def admin_manage_class(request):
    groups = Group.objects.all()
    timetables = Timetable.objects.select_related(
        'group_id', 'teacher_id', 'classroom_id'
    ).all()

    if request.method == "POST":
        method = request.POST.get("_method")
        # --- DELETE ---
        if method == "DELETE":
            timetable_id = request.POST.get("id")
            Timetable.objects.filter(id=timetable_id).delete()
            return redirect("admin_manage_class")
        # --- SEARCH ---
        elif method == "SEARCH":
            group_id = request.POST.get("group_id")
            if group_id:
                timetables = Timetable.objects.select_related(
                    'group_id', 'teacher_id', 'classroom_id'
                ).filter(group_id=group_id)
    context = {
        "groups": groups,
        "timetables": timetables,
    }
    return render(request, "admin/classes/manage_class.html", context)


def admin_add_group_schedule(request):
    groups = Group.objects.all()
    rooms = Classroom.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    timetable = Timetable()
    context = {
        "groups": groups,
        "rooms":rooms,
        "teachers":teachers,
        "subjects":subjects
    }
    if request.method == "POST":
        timetable.teacher_id = Teacher.objects.get(id=request.POST.get('teacher'))
        timetable.subject_id = Subject.objects.get(id=request.POST.get('subject'))
        timetable.group_id = Group.objects.get(id=request.POST.get('group'))
        timetable.classroom_id = Classroom.objects.get(id=request.POST.get('room'))
        timetable.start_time = request.POST.get('start_time')
        timetable.end_time = request.POST.get('end_time')
        timetable.day_of_week = request.POST.get('day')
        timetable.save()
        return redirect("admin_manage_class")
    return render(request, 'admin/classes/add_group_schedule.html',context)


def admin_add_group(request):
    if request.method == "POST":
        group = Group( )
        group_name = request.POST.get('group_name')
        group_description = request.POST.get("group_description")
        group.name = group_name
        group.description = group_description
        group.save()
        return redirect("admin_manage_class")
    return render(request, 'admin/classes/add_group.html',{})
def admin_add_room(request):
    if request.method == "POST":
        room = Classroom()
        room.name = request.POST.get('room_name')
        room.capacity = request.POST.get('room_capacity')
        room.location = request.POST.get('room_location')
        room.save()
        return redirect("admin_manage_class")
    return render(request, 'admin/classes/add_room.html',{})
    # Student Admin


# =============================== Teacher ===============================#
# Teacher Dashboard Views
def teacher_dashboard(request):
    return render(request, 'teacher/index.html',{})
def teacher_dashboard_schedule(request):
    return render(request, 'teacher/schedule.html',{})
def teacher_dashboard_attendance(request):
    return render(request, 'teacher/attendance.html',{})
def teacher_dashboard_exam(request):
    return render(request, 'teacher/exam.html',{})
def teacher_dashboard_report(request):
    return render(request, 'teacher/report.html',{})
def teacher_dashboard_inbox(request):
    return render(request, 'teacher/inbox.html',{})
# =============================== Student ===============================#
def student_dashboard(request):
    context = {
        "current_date": datetime.date.today(),
    }
    return render(request, 'student/index.html',context)
def student_dashboard_schedule(request):
    return render(request, 'student/schedule.html',{})
def student_dashboard_assignment(request):
    return render(request, 'student/assignment.html',{})
def student_dashboard_grade(request):
    return render(request, 'student/grade.html',{})
def student_dashboard_library(request):
    return render(request, 'student/library.html',{})
def student_dashboard_inbox(request):
    return render(request, 'student/inbox.html',{})


# login view
def login(request):
    if request.method == "POST":
        username = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        
        # Use environment variables or Django settings for credentials
        # This is temporary - should use proper authentication
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

# Create your views here.




# Logic for admin_function module

def enrollment_trends():
    current_date = datetime.date.today()
    def day_counter(d):
        return (current_date - d).days if d else None

    top_n = 5

    # Latest enrollments (most recent first)
    latest_enrollments = (
        Enrollment.objects
        .select_related('student_id')
        .order_by('-enrollment_date')[:top_n]
    )

    enrollment_items = []
    for e in latest_enrollments:
        student = getattr(e, 'student_id', None)
        if student:
            enrollment_items.append({
                'type': 'student',
                'name': f"{student.first_name} {student.last_name}",
                'year': e.enrollment_date.year if e.enrollment_date else None,
                'date': e.enrollment_date,
                'count': day_counter(student.start_date) if getattr(student, 'start_date', None) else None,
            })

    # Latest teachers (most recent first)
    latest_teachers = Teacher.objects.order_by('-hire_date')[:top_n]
    teacher_items = []
    for t in latest_teachers:
        teacher_items.append({
            'type': 'teacher',
            'name': f"{t.first_name} {t.last_name}",
            'year': t.hire_date.year if t.hire_date else None,
            'date': t.hire_date,
            'count': day_counter(t.hire_date) if t.hire_date else None,
        })
    combined = enrollment_items + teacher_items
    combined_sorted = sorted([c for c in combined if c.get('count')], key=lambda x: x['count'], reverse=False)
    return combined_sorted[:top_n]
