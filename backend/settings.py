import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Use a more secure secret key from environment, but fallback if not set
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-!=tda^s-5b$v1fx%z4in)zhdpr!5s(4#peidd5p+ha=^5o=1ic')

# Keep debug off in production
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database will remain SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Rest of your settings remain the same
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "exp://192.168.24.216:8081",
    "http://localhost:8081",
    "exp://localhost:8081"
]
CORS_ALLOW_ALL_ORIGINS = True