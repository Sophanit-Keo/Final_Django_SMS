from django.shortcuts import render, redirect
import datetime
from app.models import *
from .utils import enrollment_trends

# ========================= Admin Dashboard =========================
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


# ========================= Admin Classes =========================
def admin_dashboard_class(request):
    groups = Group.objects.all()
    timetable = Timetable.objects.select_related('group_id', 'teacher_id', 'classroom_id').all()
    total_groups = groups.count()
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    avg_class_size = total_students / total_groups if total_groups > 0 else 0
    context = {
        "groups": groups,
        "timetables": timetable,
        "total_groups": total_groups,
        "total_students": total_students,
        "total_teachers": total_teachers,
        "avg_class_size": avg_class_size,
    }
    return render(request, 'admin/classes/classes.html', context)


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
        "rooms": rooms,
        "teachers": teachers,
        "subjects": subjects
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
    return render(request, 'admin/classes/add_group_schedule.html', context)


def admin_add_group(request):
    if request.method == "POST":
        group = Group()
        group_name = request.POST.get('group_name')
        group_description = request.POST.get("group_description")
        group.name = group_name
        group.description = group_description
        group.save()
        return redirect("admin_manage_class")
    return render(request, 'admin/classes/add_group.html', {})


def admin_add_room(request):
    if request.method == "POST":
        room = Classroom()
        room.name = request.POST.get('room_name')
        room.capacity = request.POST.get('room_capacity')
        room.location = request.POST.get('room_location')
        room.save()
        return redirect("admin_manage_class")
    return render(request, 'admin/classes/add_room.html', {})


# ========================= Admin Teachers =========================
def admin_add_teacher(request):
    teachers = Teacher.objects.prefetch_related("subject_set").all()
    subjects = Subject.objects.all()
    teacher = Teacher()
    context = {
        "teachers": teachers,
        "subjects": subjects
    }
    if request.method == "POST":
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
    return render(request, 'admin/teacher/add_teacher.html', context)


def admin_dashboard_teacher(request):
    teachers = Teacher.objects.prefetch_related("subject_set").all()
    subjects = Subject.objects.prefetch_related("teacher_set").all()
    context = {
        "teachers": teachers,
        "subjects": subjects
    }
    if request.method == "POST":
        method = request.POST.get("_method")
        if method == "DELETE":
            teacher_id = request.POST.get("teacher_id")
            Teacher.objects.filter(id=teacher_id).delete()
            return redirect("admin_dashboard_teacher")
    return render(request, 'admin/teacher/teachers.html', context)


# ========================= Admin Students =========================
def admin_dashboard_student(request):
    students = Student.objects.prefetch_related('enrollment_set').all()
    context = {
        "current_date": datetime.date.today(),
        "students": students,
    }
    if request.method == "POST":
        method = request.POST.get('_method')
        if method == 'DELETE':
            Student.objects.filter(id=request.POST.get('student_id')).delete()
            return redirect('admin_dashboard_student')
    return render(request, 'admin/student/students.html', context)


def admin_add_student(request):
    students = Student.objects.all()
    guardians = Guardian.objects.prefetch_related("student_set").all()
    enrollments = Enrollment.objects.select_related("student_id", "subject_id", "group_id").all()
    groups = Group.objects.all()
    student_id = Student.objects.order_by('-id').values_list('id', flat=True).first() + 1
    student = Student()
    guardian = Guardian()
    enrollment = Enrollment()

    context = {
        'student_last_id': student_id,
        'students': students,
        'guardians': guardians,
        'enrollments': enrollments,
        'groups': groups
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
            context['error'] = f"Error adding student: {str(e)}"
            print(context['error'])
            return redirect('admin_add_student')

    return render(request, 'admin/student/add_student.html', context)


# ========================= Admin Reports & Schedules =========================
def admin_dashboard_report(request):
    groups = Group.objects.all()
    timetable = Timetable.objects.select_related('group_id', 'teacher_id', 'classroom_id').all()
    total_groups = groups.count()
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    avg_class_size = total_students / total_groups if total_groups > 0 else 0
    current_date = datetime.date.today()
    exams = Exam.objects.select_related().all()
    homework = Homework.objects.select_related('group_id', 'subject_id', 'teacher_id').all()
    enrollments = Enrollment.objects.select_related('student_id', 'group_id').all()

    context = {
        "groups": groups,
        "timetables": timetable,
        "total_groups": total_groups,
        "total_students": total_students,
        "total_teachers": total_teachers,
        "avg_class_size": avg_class_size,
        "current_date": current_date,
        "exams": exams,
        "homeworks": homework,
        "enrollments": enrollments,
    }
    return render(request, 'admin/report/reports.html', context)


def admin_dashboard_schedule(request):
    timetables = Timetable.objects.select_related('group_id', 'teacher_id', 'classroom_id').all()
    context = {
        "timetables": timetables,
    }
    return render(request, 'admin/schedules/schedules.html', context)
