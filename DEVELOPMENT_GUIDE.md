# Development Guidelines

## 📋 Code Organization Rules

### 1. Views (`app/view/`)
- Each role gets its own module: `admin_views.py`, `teacher_views.py`, `student_views.py`
- Auth views go in `auth_views.py`
- Utility functions go in `utils.py`
- Import all views in `__init__.py`

**Example:**
```python
# In admin_views.py
def admin_dashboard(request):
    # ...
    return render(request, "admin/indexs.html", context)

# In __init__.py
from .admin_views import *
```

### 2. URLs (`app/urls/`)
- Routes organized by module in separate files
- Each module has its own `urlpatterns` list
- Main `__init__.py` includes all patterns

**Example:**
```python
# In urls/admin.py
path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

# In urls/__init__.py
path('', include('app.urls.admin')),
```

### 3. Future: Models Organization
When `models.py` grows too large, split into:
```
app/models/
├── __init__.py
├── student.py     # Student, Guardian
├── teacher.py     # Teacher, Subject
├── academic.py    # Group, Classroom, Enrollment
├── schedule.py    # Timetable, Exam, Homework
```

### 4. Future: Forms
Create forms for validation:
```
app/forms/
├── __init__.py
├── admin_forms.py      # Admin forms
├── student_forms.py    # Student forms
├── teacher_forms.py    # Teacher forms
```

### 5. Future: Services
Extract business logic:
```
app/services/
├── __init__.py
├── enrollment_service.py
├── grade_service.py
├── report_service.py
```

## 🔄 Adding New Features

### Step 1: Create View Function
```python
# In app/view/admin_views.py or relevant module
def new_admin_feature(request):
    # Your logic here
    return render(request, 'template.html', context)
```

### Step 2: Add URL Route
```python
# In app/urls/admin.py (or relevant module)
path('new-feature/', new_admin_feature, name='new_admin_feature'),
```

### Step 3: Create Template
```html
<!-- In templates/admin/new_feature.html -->
```

### Step 4: Add Static Files (if needed)
```
static/admin/
├── css/new_feature.css
└── js/new_feature.js
```

## 📝 Naming Conventions

### Views
- Function-based: `role_section_action` (e.g., `admin_dashboard_student`)
- Clear and descriptive names

### URLs
- Use hyphens: `admin-dashboard`, `admin-add-student`
- Name attribute: `admin_dashboard` (underscores)

### Templates
- Follow folder structure: `admin/student/add_student.html`
- Use lowercase with underscores

### Static Files
- Group by role: `admin/`, `teacher/`, `student/`, `shared/`
- Clear file names: `admin.css`, `admin.js`

## ✅ Code Quality

### Do's
✅ Keep views simple and focused
✅ Move logic to `utils.py` or services
✅ Use Django ORM efficiently
✅ Use `select_related()` and `prefetch_related()`
✅ Name views and URLs clearly
✅ Comment complex logic
✅ Handle exceptions properly

### Don'ts
❌ Don't put business logic in views
❌ Don't duplicate code across views
❌ Don't use inline SQL
❌ Don't hardcode values (use settings)
❌ Don't mix concerns in one function
❌ Don't forget to update imports

## 🧪 Testing Locations

When adding tests, place them in `app/tests.py` or create a `tests/` folder:
```
app/tests/
├── __init__.py
├── test_admin_views.py
├── test_teacher_views.py
├── test_student_views.py
├── test_urls.py
```

## 🔒 Security Checklist

- [ ] Escape user input in templates
- [ ] Use Django's CSRF protection
- [ ] Hash passwords properly
- [ ] Validate form inputs
- [ ] Check user permissions
- [ ] Use `login_required` decorator
- [ ] Sanitize database queries

## 📊 Performance Tips

1. Use `select_related()` for foreign keys
2. Use `prefetch_related()` for reverse relations
3. Add database indexes for frequently queried fields
4. Cache repeated queries
5. Use pagination for large datasets
6. Minimize database queries per request

## 🚀 Deployment Checklist

- [ ] Set `DEBUG = False` in settings
- [ ] Update `ALLOWED_HOSTS`
- [ ] Set secret key in environment variable
- [ ] Configure static file serving
- [ ] Set up logging
- [ ] Enable HTTPS
- [ ] Configure email backend
- [ ] Set up database backups
- [ ] Use environment-based settings

## 📚 Useful Commands

```bash
# Create migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Create custom management command
python manage.py startapp myapp
```
