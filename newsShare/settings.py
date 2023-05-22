from pathlib import Path
import os
import cloudinary
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4bgmj$_4g^=ntqecal6(-&0h#uk_a-mo_rqo&mdm#lbz3=ym$a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'main',
    'ckeditor',
    "debug_toolbar",
    'cloudinary',
    'cloudinary_storage',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'newsShare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'newsShare.wsgi.application'





# Password validation
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL='media/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'media')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if DEBUG==True:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }
    MEDIA_ROOT=os.path.join(BASE_DIR,'media_cdn')
    STATIC_ROOT=os.path.join(BASE_DIR,'static_cdn')
    
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neondb',
        'USER': 'theronalliance.dev',
        'PASSWORD': '6yoOK3HpXStA',
        'HOST': 'ep-steep-snow-436674.us-east-2.aws.neon.tech',
        'PORT': '5432',
    }
    }
    CLOUDINARY_STORAGE={
        'CLOUD_NAME': 'dz5t3boez',
        'API_KEY': '128332246382333',
        'API_SECRET': os.environ.get('API_SECRET'),
    }
    cloudinary.config( 
        cloud_name = "dz5t3boez", 
        api_key = "128332246382333", 
        api_secret = os.environ.get('API_SECRET'), 
        )
    DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

    STATIC_URL='https://foreverinc.github.io/Newsstatic_cdn/'
        
INTERNAL_IPS = [
        "127.0.0.1",
    ]   


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'theronalliance.dev@news.com'
EMAIL_HOST_PASSWORD = 'gksznagmjpkzikfg'
EMAIL_USE_TLS = True
 
 

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"    
