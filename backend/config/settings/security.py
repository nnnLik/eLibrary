import os

from .base import BASE_DIR


SECRET_KEY = "django-insecure-l^i#377)m(@y&rv0qfpbo&uru_#^zo6nt)*mvroi@xx671=nf#"

DEBUG = True

ALLOWED_HOSTS = ["*"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:4200",
    "http://localhost:1313",
    "http://localhost:4200",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SSL_KEY_PATH = os.path.join(BASE_DIR, 'certs', 'key.pem')
SSL_CERTIFICATE_PATH = os.path.join(BASE_DIR, 'certs', 'cert.pem')

SERVER_SETTINGS = {
    'BIND_ADDRESS': ('your_domain', 8888),
    'SSL_CERTIFICATE': SSL_CERTIFICATE_PATH,
    'SSL_PRIVATE_KEY': SSL_KEY_PATH,
    'WSGI_APPLICATION': 'your_project.wsgi:application',
}

USE_SSL = True
