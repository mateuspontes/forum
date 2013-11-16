import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '9kf5!yl4ts-yor12^l6$xm+0#5bhkl^qqjhojzs*86t=!etk6v'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
  'djangocms_admin_style',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'home',
  'questions',
)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'forum.urls'

WSGI_APPLICATION = 'forum.wsgi.application'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'questions',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
  }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/assets/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
  os.path.join(BASE_DIR, "templates"),
)