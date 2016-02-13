import os

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

DEBUG = bool(os.getenv('DEBUG', 0))

EMAIL = os.getenv('EMAIL') or 'bot@dogood.com'
PASSWORD = os.getenv('PASSWORD') or 'secret'
OWNER_ID = os.getenv('OWNER_ID')

SECRET_KEY = os.getenv('SECRET_KEY', 'i-am-very-secret')

LOGGING_CONFIG = 'logging.config.dictConfig'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(process)d %(thread)d  %(message)s'
        },
        'timestamped': {
            'format': '%(asctime)s %(levelname)s %(name)s  %(message)s'
        },
        'simple': {
            'format': '%(levelname)s  %(message)s'
        },
        'performance': {
            'format': '%(asctime)s %(process)d | %(thread)d | %(message)s',
        },
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'timestamped',
        },
    },
    'loggers': {
        'bot': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'discord.db',
    }
}


INSTALLED_APPS = [
    'bot.plugins.game_notifications',
    'bot.plugins.reddit',
    'bot.plugins.status',
    'bot.users',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]


PRAW_USER_AGENT = 'python:discord-fetcher:v0.0.1 (by /u/xBBTx)'


PLUGINS = {
    'daisy': {
        'enabled': True,
        'subreddit': 'DaisyRidley',
        'useragent': PRAW_USER_AGENT,
    },
    'log': {
        'enabled': True,
    },
    'game_notifications': {
        'enabled': True,
    },
    'help': {
        'enabled': True,
    },
    'test': {
        'enabled': False,
    },
    'system': {
        'enabled': True,
    },
    'random_commands': {
        'enabled': True,
    },
    'reddit': {
        'enabled': True,
        'useragent': PRAW_USER_AGENT,
    },
    'til': {
        'enabled': True,
        'subreddit': 'todayilearned',
        'useragent': PRAW_USER_AGENT,
    },
    'status': {
        'enabled': True,
    }
}


ROOT_URLCONF = 'bot.urls'
