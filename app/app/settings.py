import environ
from pathlib import Path
from django.utils.translation import ugettext_lazy as _

env = environ.Env()

""" make use of django-environ to store environment variables
outside version control (must include the file name in .gitignore for git);
two type of variables need to be stored at envirenment dependent location;
1. the secret keys that must be hidden for secutity reasons and
2. the variables with different value in production/development envirenment,
for example DEBUG and TEMPLATE_DEBUG are True during development,
but should be False in production again for security reasons """

env.read_env()

SECRET_KEY = env('SECRET_KEY', default = 'secret key not found')
ENCRYPT_KEY = env('ENCRYPT_KEY', default = 'encrypt key not found')
DEBUG = env.bool('DJANGO_DEBUG', default = False)
is_prod = env.bool('IS_PRODUCTION', default = True)

is_dev = not is_prod # vive la france
TEMPLATE_DEBUG = DEBUG

BASE_DIR = Path(__file__).resolve().parent.parent
# build paths inside the project like this: BASE_DIR / 'subdir'
# PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = ['*'] # not safe
SILENCED_SYSTEM_CHECKS = ["security.W004", "security.W008"]
INTERNAL_IPS = ['ka.lo', '127.0.0.3']
SESSION_COOKIE_SECURE = True

if is_prod:
	ALLOWED_HOSTS = ['.kalodev.site', '142.93.171.130']
else: # is_dev:
	ALLOWED_HOSTS = INTERNAL_IPS
	SESSION_COOKIE_SECURE = False # needed by admin in development
	SILENCED_SYSTEM_CHECKS.extend(["security.W012", "security.W018"])

CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False # SSL_REDIRECT = True does not work, but ...
# SECURE_HSTS_SECONDS = 6 # ... one may try with SECURE_HSTS_SECONDS
X_FRAME_OPTIONS = 'SAMEORIGIN' # enable frames
X_FRAME_OPTIONS = 'DENY' # disable frames

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
			'formatter': 'console'
        },
        'file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
			'formatter': 'file',			
            'filename': BASE_DIR / 'log/django.log'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    },
}

# Application definition
INSTALLED_APPS = [
	'rest_framework',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'debug_toolbar',
	'bootstrap4',
	'django_extensions',
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

def show_toolbar(request): return DEBUG
DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
						'INTERCEPT_REDIRECTS': False}
if DEBUG:
	import mimetypes
	mimetypes.add_type("application/javascript", ".js", True)
	mimetypes.add_type("image/png", ".png", True)
	mimetypes.add_type("image/jpg", ".jpg", True)
	mimetypes.add_type("image/x-icon", ".ico", True)
	mimetypes.add_type("image/svg+xml", ".svg", True)
	mimetypes.add_type("text/css", ".css", True)
	mimetypes.add_type("text/plain", ".txt", True)

# DEBUG_TOOLBAR_PANELS = [
# 	'debug_toolbar.panels.versions.VersionsPanel',
# 	'debug_toolbar.panels.timer.TimerPanel',
# 	'debug_toolbar.panels.settings.SettingsPanel',
# 	'debug_toolbar.panels.headers.HeadersPanel',
# 	'debug_toolbar.panels.request.RequestPanel',
# 	'debug_toolbar.panels.sql.SQLPanel',
# 	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
# 	'debug_toolbar.panels.templates.TemplatesPanel',
# 	'debug_toolbar.panels.cache.CachePanel',
# 	'debug_toolbar.panels.signals.SignalsPanel',
# 	'debug_toolbar.panels.logging.LoggingPanel',
# 	'debug_toolbar.panels.redirects.RedirectsPanel'
# ]

MIDDLEWARE = [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware', # you
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
USE_I18N = USE_L10N = USE_TZ = True

LOCALE_PATHS = (BASE_DIR / 'locale', BASE_DIR / 'i18n')
LANGUAGES = [('en', _('English')), ('fr', _('French'))]
LANGUAGE_CODE = 'fr'
LANGUAGE_BIDI = False
TIME_ZONE = 'Europe/Paris'

# static server
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
ENCRYPT_URL = '/.well-known/'
ENCRYPT_ROOT = STATIC_ROOT / '.well-known/'
ROBOTS_URL = '/robots.txt/'
ROBOTS_ROOT = STATIC_ROOT / 'robots.txt'
FAVICON_URL = '/favicon.ico/'
FAVICON_ROOT = STATIC_ROOT / 'ico/favicon.ico'
CV_URL = '/cv/'
CV_ROOT = STATIC_ROOT / 'pdf/back-end.pdf'
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

X_FRAME_OPTIONS = 'SAMEORIGIN'

système code signification
W004 SECURE_HSTS_SECONDS not set
W008 SECURE_SSL_REDIRECT not True
W012 SESSION_COOKIE_SECURE not True
W018 DEBUG is True

"""
