# School Management System (SMS) - Project Structure

## 📁 Project Organization

```
Final_Django/
├── manage.py                          # Django CLI
├── requirements.txt                   # Project dependencies
├── README.md                          # Project documentation
├── .env                              # Environment variables
├── .gitignore                        # Git ignore rules
│
├── SMS/                              # Main Django project settings
│   ├── settings.py                   # Django configuration
│   ├── urls.py                       # Main URL router
│   ├── asgi.py                       # ASGI config
│   ├── wsgi.py                       # WSGI config
│   └── __init__.py
│
├── app/                              # Main application
│   ├── models.py                     # Database models
│   ├── admin.py                      # Django admin config
│   ├── apps.py                       # App configuration
│   ├── tests.py                      # Test cases
│   ├── __init__.py
│   │
│   ├── view/                         # Views organized by module
│   │   ├── __init__.py               # Exports all views
│   │   ├── admin_views.py            # Admin dashboard views (13 functions)
│   │   ├── teacher_views.py          # Teacher views (6 functions)
│   │   ├── student_views.py          # Student views (6 functions)
│   │   ├── auth_views.py             # Authentication views (2 functions)
│   │   └── utils.py                  # Helper functions (enrollment_trends)
│   │
│   ├── urls/                         # URL routing organized by module
│   │   ├── __init__.py               # Combines all URL patterns
│   │   ├── admin.py                  # Admin routes (12 paths)
│   │   ├── teacher.py                # Teacher routes (6 paths)
│   │   ├── student.py                # Student routes (6 paths)
│   │   └── auth.py                   # Auth routes (login/logout)
│   │
│   ├── models/                       # Database models (organized)
│   │   └── __init__.py               # For future model organization
│   │
│   ├── forms/                        # Django forms
│   │   └── __init__.py               # For future form classes
│   │
│   ├── services/                     # Business logic services
│   │   └── __init__.py               # For service classes
│   │
│   ├── middleware/                   # Custom middleware
│   │   └── __init__.py               # For custom middleware
│   │
│   ├── decorators/                   # Custom decorators
│   │   └── __init__.py               # For custom decorators
│   │
│   ├── migrations/                   # Database migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   │
│   └── __pycache__/
│
├── templates/                        # HTML templates
│   ├── login.html                    # Login page
│   ├── admin/                        # Admin templates
│   │   ├── indexs.html
│   │   ├── classes/
│   │   │   ├── add_group.html
│   │   │   ├── add_group_schedule.html
│   │   │   ├── add_room.html
│   │   │   ├── classes.html
│   │   │   └── manage_class.html
│   │   ├── student/
│   │   │   ├── add_student.html
│   │   │   └── students.html
│   │   ├── teacher/
│   │   │   ├── add_teacher.html
│   │   │   └── teachers.html
│   │   ├── report/
│   │   │   └── reports.html
│   │   └── schedules/
│   │       └── schedules.html
│   ├── student/                     # Student templates
│   │   ├── index.html
│   │   ├── assignment.html
│   │   ├── grade.html
│   │   ├── inbox.html
│   │   ├── library.html
│   │   └── schedule.html
│   ├── teacher/                     # Teacher templates
│   │   ├── index.html
│   │   ├── attendance.html
│   │   ├── exam.html
│   │   ├── inbox.html
│   │   ├── report.html
│   │   └── schedule.html
│   ├── layout/                      # Base layout templates
│   │   ├── admin_sidebar.html
│   │   ├── student_sidebar.html
│   │   ├── teacher_sidebar.html
│   │   └── components/
│   └── parent/
│
├── static/                          # Static files (CSS, JS)
│   ├── admin/
│   │   ├── css/
│   │   │   ├── admin.css
│   │   │   ├── login.css
│   │   │   ├── student.css
│   │   │   └── teacher.css
│   │   └── js/
│   │       ├── admin.js
│   │       ├── classes.js
│   │       └── student.js
│   ├── login/
│   │   └── login.js
│   └── shared/
│       ├── css/
│       │   ├── components.css
│       │   ├── layout.css
│       │   ├── reset.css
│       │   └── typography.css
│       └── js/
│           ├── charts.js
│           ├── sidebar.js
│           └── utils.js
│
└── venv/                            # Virtual environment (do not commit)
```

## 🏗️ Architecture

### Views Layer (`app/view/`)
- **admin_views.py**: Admin dashboard and management views
- **teacher_views.py**: Teacher dashboard views
- **student_views.py**: Student dashboard views
- **auth_views.py**: Login/logout authentication
- **utils.py**: Helper functions and utilities

### URL Routing (`app/urls/`)
- **__init__.py**: Main URL aggregator
- **admin.py**: Admin routes
- **teacher.py**: Teacher routes
- **student.py**: Student routes
- **auth.py**: Authentication routes

### Database (`app/models.py`)
- Student, Teacher, Guardian models
- Group, Classroom, Subject models
- Enrollment, Timetable, Exam, Homework models

### Templates (`templates/`)
- Organized by user role (admin, teacher, student)
- Shared layout components
- Static includes (CSS, JS)

### Static Files (`static/`)
- Role-specific CSS and JavaScript
- Shared utility styles and scripts

## 📋 View Functions Count
- **Admin**: 13 functions
- **Teacher**: 6 functions
- **Student**: 6 functions
- **Auth**: 2 functions
- **Total**: 27 functions

## 🔗 URL Routes Count
- **Admin**: 12 routes
- **Teacher**: 6 routes
- **Student**: 6 routes
- **Auth**: 2 routes
- **Total**: 26 routes

## 🚀 Running the Project

```bash
# Activate virtual environment
source venv/Scripts/activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access the application
http://localhost:8000
```

## 📝 Key Features

1. **Role-Based Access**
   - Admin Dashboard
   - Teacher Dashboard
   - Student Dashboard

2. **Admin Management**
   - Student management
   - Teacher management
   - Class/Group management
   - Classroom management
   - Timetable scheduling
   - Reports and analytics

3. **Teacher Features**
   - Schedule viewing
   - Attendance tracking
   - Exam management
   - Report generation
   - Inbox

4. **Student Features**
   - Schedule viewing
   - Assignment submission
   - Grade viewing
   - Library access
   - Inbox

## 🔐 Security Notes

- Currently using hardcoded credentials (temporary)
- TODO: Implement proper authentication system
- TODO: Add password hashing
- TODO: Add user sessions
- TODO: Add CSRF protection on all forms

## 📦 Future Organization Opportunities

1. **Models**: Split `models.py` into separate files by entity
2. **Forms**: Create Django forms for validation
3. **Services**: Extract business logic into service classes
4. **Middleware**: Add custom middleware for authentication
5. **Decorators**: Create decorators for view protection
6. **Tests**: Organize tests by module
7. **Signals**: Add Django signals for model events
8. **Management**: Add custom management commands

## 💡 Best Practices Implemented

✅ Views organized by role/feature
✅ URLs in dedicated folder
✅ Clear separation of concerns
✅ Modular structure for scalability
✅ Easy to add new features
✅ Easy for team collaboration
✅ Professional Django project structure
