"""Configuración de la Evaluación 2: Django + DRF y variables de entorno."""
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
# Las variables del sistema prevalecen sobre las del archivo local .env.
load_dotenv(BASE_DIR / ".env", override=False)

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "").strip()
if not SECRET_KEY:
    raise ImproperlyConfigured(
        "Falta DJANGO_SECRET_KEY. Copia .env.example a .env y configura la clave."
    )

DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() in ("true", "1", "yes", "si")
ALLOWED_HOSTS = [host.strip() for host in os.getenv(
    "DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,testserver"
).split(",") if host.strip()]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "widget_tweaks",
    "tasks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ]
    },
}]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

DB_ENGINE = os.getenv("DB_ENGINE", "sqlite").lower().strip()
if DB_ENGINE in ("sqlite", "sqlite3"):
    sqlite_name = os.getenv("DB_NAME", "db.sqlite3") or "db.sqlite3"
    db_path = Path(sqlite_name)
    DATABASES = {"default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": db_path if db_path.is_absolute() else BASE_DIR / db_path,
    }}
elif DB_ENGINE in ("postgres", "postgresql", "mariadb", "mysql"):
    backend = ("django.db.backends.postgresql"
               if DB_ENGINE in ("postgres", "postgresql")
               else "django.db.backends.mysql")
    DATABASES = {"default": {
        "ENGINE": backend,
        "NAME": os.getenv("DB_NAME", "gestor_tareas_db"),
        "USER": os.getenv("DB_USER", "gestor_tareas_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432" if backend.endswith("postgresql") else "3306"),
    }}
    if backend.endswith("mysql"):
        DATABASES["default"]["OPTIONS"] = {"charset": "utf8mb4"}
else:
    raise ImproperlyConfigured(
        "DB_ENGINE debe ser sqlite, postgresql o mariadb/mysql."
    )

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

REST_FRAMEWORK = {
    # API abierta para pruebas académicas LOCALES; no desplegar públicamente sin autenticación.
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
