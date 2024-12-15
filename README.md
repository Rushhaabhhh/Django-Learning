# Django Framework

Django is a high-level Python web framework that enables rapid development of secure and scalable web applications. It emphasizes reusability, less code duplication, and follows the "Don't Repeat Yourself" (DRY) principle.

## Features

- **ORM**: Built-in Object-Relational Mapping for database interactions.
- **Security**: Prevents common vulnerabilities like XSS, CSRF, and SQL injection.
- **Scalability**: Modular components for scaling applications.
- **Admin Interface**: Auto-generated admin panel for managing data.
- **URL Routing**: Clear and clean URL configurations.
- **Templating Engine**: Flexible templates for frontend development.
- **Third-party Support**: A rich ecosystem of reusable packages.

---

## Installation

1. Install Django using pip :
```bash
pip install django
```

2. Verify the installation:
```bash
python -m django --version
```

## Getting Started : 

1. Create a Project : 
```bash
django-admin startproject project_name
```

2. Run the Development Server:

```bash
python manage.py runserver
```
- Visit http://127.0.0.1:8000/ in your browser.

3. Create an App:

```bash
python manage.py startapp app_name
```

4. Configure Settings :
- Add your app to INSTALLED_APPS in settings.py.

## Basic Commands

1. Migrate Database:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Run Tests:

```bash
python manage.py test
```

2. Create Superuser:

```bash
python manage.py createsuperuser
```