from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

# build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*'] # not safe
is_production = env.bool('IS_PRODUCTION', default = True)

if is_production:
	ALLOWED_HOSTS = ['.kalodev.site', '142.93.171.130']
	SESSION_COOKIE_SECURE = True
else: # is_development:
	ALLOWED_HOSTS = ['ka.lo', '127.0.0.3']
	SESSION_COOKIE_SECURE = False # needed for admin in development

SECRET_KEY = env('SECRET_KEY', default = 'secret key not found')
ENCRYPT_KEY = env('ENCRYPT_KEY', default = 'encrypt key not found')
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False # SSL_REDIRECT = True does not work, but ...
# SECURE_HSTS_SECONDS = 6 # ... one may try with SECURE_HSTS_SECONDS
DEBUG = env.bool('DJANGO_DEBUG', default = False)
TEMPLATE_DEBUG = DEBUG

# Application definition
INSTALLED_APPS = [
	'rest_framework',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'memo',
	'work',
	'news'
]

REST_FRAMEWORK = {
	# Use Django's standard `django.contrib.auth` permissions,
	# or allow read-only access for unauthenticated users.
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	]
}

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [ BASE_DIR / 'templates' ],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'app.context_processors.get_context',
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages'
			]
		},
	},
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True
#X_FRAME_OPTIONS = 'SAMEORIGIN'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
ENCRYPT_URL = '/.well-known/'
ENCRYPT_ROOT = STATIC_ROOT / '.well-known/'
LOGIN_URL = '/admin/login/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 6
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = False
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_DOMAIN = '127.0.0.3'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 86400 # sec
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'DSESSIONID'
SESSION_COOKIE_SECURE = False
"""
