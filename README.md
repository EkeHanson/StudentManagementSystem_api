# 📘 Excel International Excellent Schools - Student Management System (SMS)

A **Student Management System (SMS)** built with **Django** and **Django REST Framework (DRF)** to streamline administrative tasks, manage student records, and facilitate communication between students, teachers, parents, and administrators.

## 🚀 Features

### Core Functionalities
1. **User Management & Authentication**  
   - Role-based access: Admin, Teachers, Students, Parents.  
   - Secure login, password reset, and multi-factor authentication (optional).  
   - Profile management with photos and personal details.

2. **Student Information Management**  
   - Registration, class assignment, attendance, and progress tracking.  
   - ID card generation, health records, and disciplinary logs.

3. **Teacher Management**  
   - Teacher profiles, subject/class assignments, and attendance tracking.

4. **Parent Portal**  
   - View child performance, pay fees online, and communicate with teachers/admin.

5. **Academic Management**  
   - Timetable creation, syllabus management, homework/assignments, grading, and report cards.

6. **Attendance Management**  
   - Daily or class-wise attendance with notifications for absenteeism.

7. **Fee Management**  
   - Define fee structures, enable online payments, and track payments.

8. **Library Management**  
   - Book catalog, borrowing/return tracking, and overdue alerts.

9. **Transport Management**  
   - Bus routes, schedules, and optional GPS tracking.

10. **Communication & Notifications**  
   - Internal messaging and email/SMS alerts.

11. **Reports & Analytics**  
   - Performance analytics, fee tracking, attendance reports, and examination results.

---

## 🏗️ Project Structure

```plaintext
myschool/
├── myschool/                  # Project configuration files
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configurations
│   ├── wsgi.py                # WSGI configuration
│   ├── asgi.py                # ASGI configuration
│   └── __init__.py
├── apps/                      # All Django apps
│   ├── user_management/       # User roles and authentication
│   ├── student_management/    # Student registration and records
│   ├── teacher_management/    # Teacher profiles and classes
│   ├── parent_portal/         # Parent features
│   ├── academic_management/   # Timetables, grades, assignments
│   ├── attendance_management/ # Attendance tracking
│   ├── fee_management/        # Fee structures and payments
│   ├── library_management/    # Library features
│   ├── transport_management/  # Transport and routes
│   ├── notifications/         # Email and messaging
│   ├── reports_analytics/     # Reporting and analytics
├── templates/                 # HTML templates for frontend
├── static/                    # Static files (CSS, JS, images)
├── media/                     # Uploaded files (images, documents)
├── manage.py                  # Django management CLI
└── requirements.txt           # Python dependencies
```

---

## 🛠️ Installation and Setup

### Prerequisites
- Python 3.9+
- PostgreSQL/MySQL (or SQLite for local development)
- Node.js (for optional frontend integration)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/sms.git
   cd sms
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
 env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**
   - Edit `myschool/settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the App**
   Open your browser and visit [http://127.0.0.1:9090](http://127.0.0.1:9090).

---

## 🧩 API Endpoints

The project uses **Django REST Framework** for API development. Below are key endpoints:

### Authentication
- `POST /api/auth/login/`  
- `POST /api/auth/logout/`  
- `POST /api/auth/register/`

### User Management
- `GET /api/users/` (Admin-only)  
- `GET /api/users/{id}/`  

### Student Management
- `GET /api/students/`  
- `POST /api/students/`  
- `PATCH /api/students/{id}/`  

### Attendance
- `GET /api/attendance/`  
- `POST /api/attendance/mark/`  

### Fee Management
- `GET /api/fees/`  
- `POST /api/fees/pay/`  

_For the full API documentation, visit `/api/docs`._

---

## 📚 Technologies Used
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (or SQLite for local development)
- **Frontend (Optional)**:   React.js)
- **Authentication**: Django Allauth/Custom Auth
- **Deployment**: Gunicorn  (production-ready setup)

---

## 🌟 Contributing

We welcome contributions! Follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Added feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For questions or support, email: **support@excelschools.com**  
Website: [Excel International Excellent Schools](https://www.excelschools.com)  

Happy coding! 🎉