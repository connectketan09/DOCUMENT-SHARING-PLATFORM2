import os
from pathlib import Path
import secrets

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 SECURITY
SECRET_KEY = secrets.token_urlsafe(50)

DEBUG = True  # change to False after deploy

ALLOWED_HOSTS = ['*']  # change later to your domain

# 🔧 APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shareapp',
]

# 🔧 MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# 🔗 URL
ROOT_URLCONF = 'docshare_project.urls'

# 🎨 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ⚙️ WSGI
WSGI_APPLICATION = 'docshare_project.wsgi.application'

# 🗄️ DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 📦 STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# 📁 MEDIA FILES (IMPORTANT FOR QR + UPLOAD)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# 🔢 DEFAULT FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'