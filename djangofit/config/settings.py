"""Definição do projeto"""

from pathlib import Path

from decouple import Csv, UndefinedValueError, config
from dj_database_url import parse as dburl

BASE_DIR = Path(__file__).resolve().parent.parent

APP_DIR = BASE_DIR / "djangosige"


# === Configurações centrais === #
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# === Banco de dados === #
try:
    DATABASES = {
        "default": config("DATABASE_URL", cast=dburl),
    }
except UndefinedValueError:
    DATABASES = {
        "default": {
            "ENGINE": config("SQL_ENGINE"),
            "NAME": config("SQL_NAME"),
            "USER": config("SQL_USER"),
            "PASSWORD": config("SQL_PASSWORD"),
            "HOST": config("SQL_HOST"),
            "PORT": config("SQL_PORT"),
        }
    }

# === Debugging === #
DEBUG = config("DEBUG", cast=bool)

# === E-mail === #
DEFAULT_FROM_EMAIL = "webmaster@localhost"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
EMAIL_USE_SSL = config("EMAIL_USE_SSL")

# === File Uploads === #
MEDIA_URL = "media/"

MEDIA_ROOT = BASE_DIR / "media/"

# === Internacionalização === #
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True
USE_TZ = True

# === HTTP === #
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

# === Modelos === #
FIXTURE_DIRS = [
    BASE_DIR / "fixtures",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_APPS = []
LOCAL_APPS = []
INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS

# === Segurança === #
SECRET_KEY = config("SECRET_KEY")

# === Templates === #
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === URLs === $
ROOT_URLCONF = "config.urls"

# === Usuário e Autenticação === #
AUTH_USER_MODEL = "auth.User"
LOGIN_REDIRECT_URL = "/accounts/login/"
LOGIN_URL = "/accounts/login/"
LOGOUT_REDIRECT_URL = ""
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
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

# === Arquivos estátivos === #
STATIC_URL = "static/"

