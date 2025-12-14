import datetime
from app.models import Enrollment, Teacher

# ========================= Helper Functions =========================
def enrollment_trends():
    """Get the latest enrollment and teacher hiring trends"""
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
