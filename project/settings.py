"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h8xl)q9qf02vo9!gj3#--g+x7u^)ay*fanuz357&yr-(@n&2mn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
}


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
        
    ]
}

# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'taggit',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'debug_toolbar',
    'orders',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    
    #your app
    'products',
    'settings',
    'django_bootstrap5',      
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "context_cache.middleware.ContextCacheMiddleware",
    "allauth.account.middleware.AccountMiddleware",
 
]

ROOT_URLCONF = 'project.urls'

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings.settings_context_processor.get_settings',
                'orders.cart_context_processor.get_cart_data',
                ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

""" 
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Amazon",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
    }
}
 """# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",]

MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

""" 
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
"""
 
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379/0",
    }
}
 


""" 
#celery and redis
CELERY_BROKER_URL='redis://127.0.0.1:6379'
CELERY_BACKEND_RESULTS='redis://127.0.0.1:6379'
 """
  
#celery and redis in docker
CELERY_BROKER_URL='redis://redis:6379/0'
CELERY_BACKEND_RESULTS='redis://redis:6379/0'

LOGIN_REDIRECT_URL = '/'



AUTHENTICATION_BACKENDS= ['accounts.backend.EmailOrUsernameLogin',
]


#translation
LOCALE_PATHS=['locale']

LANGUAGES = [
    ("ar", "Arabic"),
    ("en", "English"),
]









#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" to check email from terminal
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
#EMAIL_HOST_PASSWORD ='gurstnsjoaxxwuyu'
EMAIL_HOST_USER ='noor539cc@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 
EMAIL_USE_SSL = False 







STRIPE_API_KEY_PUBLISHABLE='pk_test_51P7vplRw9JofhpOlVrQQV3Nwf36ET0CuJeZuYAfcddCCc3Xtid4CU53RXRDw5twhtRTVK5q7UjNokd8g1WofYE5N00EwSsVDO6'
STRIPE_API_KEY_SECRET='sk_test_51P7vplRw9JofhpOlolmIPLmYLRyyEJJDtwVuMhqkZVJem1iFA1K6pc7tWzfUcsXX17CpouX55Ph4l9mf12kDwv0y00e9aWG9hz'



