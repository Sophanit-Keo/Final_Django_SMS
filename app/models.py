from django.db import models

# Create your models here.
# Model for Student
class Student(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=20)
    special_needs = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    school_email = models.EmailField(unique=True)
    user_id = models.IntegerField(default=1)

    # foreign keys
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Model for Teacher
class Teacher(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    hire_date = models.DateField()
    status = models.CharField(max_length=20)
    school_email = models.EmailField(unique=True)
    user_id = models.IntegerField(default=1)
    # foreign keys


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Model for Subject
class Subject(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    # foreign key
    teacher_id = models.ManyToManyField(Teacher)


    def __str__(self):
        return self.name
    
# Model for Group
class Group(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # foreign keys

    def __str__(self):
        return self.name
# Model for Attendance
class Attendance(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    status = models.CharField(max_length=20)
    # foreign keys
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return f"Attendance of {self.student_id} on {self.date}"
    

# Model for Classroom
class Classroom(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    # foreign keys

    def __str__(self):
        return self.name

# Model for Enrollment
class Enrollment(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=20)
    # foreign keys
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_id} enrolled in {self.group_id}"
# Model for Exam
class Exam(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    total_marks = models.IntegerField()
    # foreign keys


    def __str__(self):
        return f"Exam: {self.name}" 
    
# Model for Grade
class Grade(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    score = models.FloatField()
    letter_grade = models.CharField(max_length=2)
    date_recorded = models.DateField()
    # foreign keys
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f"Grade of {self.student_id} in {self.subject_id}: {self.letter_grade}"
    

# Model for Guardian
class Guardian(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    # foreign keys
    student_id = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.relationship}"
    
# Model for Homework
class Homework(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_date = models.DateField()
    due_date = models.DateField()
    # foreign keys
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
# Model for HomeworkSubmission
class HomeworkSubmission(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    submission_date = models.DateField()
    content = models.TextField()
    # foreign keys
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return f"Submission by {self.student_id} for {self.homework_id}"
# Model for Timetable
class Timetable(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    # foreign keys
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"Timetable for {self.group_id} on {self.day_of_week}"
