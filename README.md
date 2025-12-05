# Django School Management System (SMS)

A comprehensive Django-based School Management System designed to streamline administrative tasks, manage students, teachers, classes, schedules, grades, and attendance.

## Features

- **User Authentication**: login system for Admin, Teachers, and Students (completed)
- **Admin Dashboard**: Manage classes, students, teachers, schedules, and generate reports (not yet complete)
- **Student Portal**: View grades, assignments, schedules, library resources, and inbox (view only)
- **Teacher Portal**: Manage attendance, exams, grades, reports, schedules, and inbox (view only)
- **Class Management**: Add groups, rooms, and manage class schedules (completed)
- **Grade Management**: Track and manage student grades and assignments (view only)
- **Attendance Tracking**: Record and monitor student attendance (view only)
- **Exam Management**: Create and manage exams for different classes (view only)
- **Responsive Design**: Mobile-friendly user interface (view only)

## Project Structure
```
Django_SMS/
├── SMS/                    # Project settings and configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── app/                    # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── admin.py           # Admin panel configuration
│   ├── migrations/        # Database migrations
│   └── tests.py           # Unit tests
├── templates/             # HTML templates
│   ├── login.html         # Login page
│   ├── admin/             # Admin templates
│   ├── student/           # Student templates
│   ├── teacher/           # Teacher templates
│   └── layout/            # Shared layout templates
├── static/                # Static files
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── admin/             # Admin static files
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sophanit-Keo/Django_School_Management-_System.git
   cd Django_SMS
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`
   - Super_Admin panel: `http://localhost:8000/supper-admin/`

## Usage

### Admin Features
- Manage students, teachers, and classes ✅
- Create and manage schedules ✅
- Add rooms and class groups ✅
- Generate reports ❌

### Student Features (View Only Function not work yet)
- View personal dashboard 
- Check grades and assignments 
- View schedule 
- Access library resources 
- Manage inbox messages 

### Teacher Features (View Only Function not work yet)
- Track student attendance 
- Create and manage exams 
- View and update grades 
- Generate reports 
- Manage schedule 
- Send messages to students

## Requirements

Key dependencies:
- Django 3.2+
- MySQL (default database)
- Python standard library modules

For a complete list, see `requirements.txt`

## Git Workflow

```bash
# Check current branch
git branch

# Switch branch
git checkout branch-name

# Create new branch
git checkout -b new-branch-name

# Push changes
git push origin branch-name

# Merge branches
git merge branch-name
```

## Branches

- **master**: Initial stable release

## Troubleshooting

### Database Issues
If you encounter database issues, reset the database:
```bash
python manage.py flush
python manage.py migrate
python manage.py createsuperuser
```

### Missing Migrations
Apply pending migrations:
```bash
python manage.py migrate
```

### Module Not Found
Ensure virtual environment is activated and all requirements are installed:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- [ ] Teacher Feature 
- [ ] Student Feature
- [ ] Advanced reporting features
- [ ] Parent portal

## Contributing

1. Create a new branch for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them
   ```bash
   git commit -m "Add your feature description"
   ```

3. Push to your branch
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request

## License

This study purpose only

## Contact & Support

For questions or support, please contact:
- GitHub: [@Sophanit-Keo](https://github.com/Sophanit-Keo)
- Repository: [Django_School_Management-_System](https://github.com/Sophanit-Keo/Django_School_Management-_System)

---

**Version**: 1.0.0  
**Last Updated**: December 2025
