from pathlib import Path
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Inicializa o carregador .env
env = Env()
env.read_env(f"{BASE_DIR}/.env.{env.str('DJANGO_ENV', 'dev')}")

# Configurações principais
SECRET_KEY = env.str("SECRET_KEY", "unsafe-default-key")
DEBUG = env.bool("DEBUG", False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", ["*"])

# Aplicações instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "recipes",
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

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "base_templates",
            BASE_DIR / "recipes" / "templates_temp",
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

WSGI_APPLICATION = "core.wsgi.application"

# Banco de dados
DATABASES = {
    "default": {
        "ENGINE": env.str("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": env.str("DB_NAME", str(BASE_DIR / "db.sqlite3")),
        "USER": env.str("DB_USER", ""),
        "PASSWORD": env.str("DB_PASSWORD", ""),
        "HOST": env.str("DB_HOST", ""),
        "PORT": env.str("DB_PORT", ""),
    }
}

# Configurações regionais
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
