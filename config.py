# -*- coding: utf-8 -*-
import os

from .common import *   # noqa, pylint: disable=unused-wildcard-import

#########################################
## GENERIC
#########################################

DEBUG = False
#SESSION_COOKIE_SECURE = False
#CSRF_COOKIE_SECURE = False

#ADMINS = (
#    ("Admin", "example@example.com"),
#)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'taiga',
        'HOST': 'taiga-db',
        'PORT': '',
    }
}

SECRET_KEY = "taiga-back-secret-key"
TAIGA_URL = "http://trego.trigonsa.net:9000"
SITES = {
    "api": {"domain": "trego.trigonsa.net", "scheme": "http", "name": "api"},
    "front": {"domain": "trego.trigonsa.net", "scheme": "http", "name": "front"}
}

# Setting DEFAULT_PROJECT_SLUG_PREFIX to false
# removes the username from project slug
DEFAULT_PROJECT_SLUG_PREFIX = False

#########################################
## MEDIA AND STATIC
#########################################

# MEDIA_ROOT = '/home/taiga/media'
MEDIA_URL = f"{ TAIGA_URL }/media/"
DEFAULT_FILE_STORAGE = "taiga_contrib_protected.storage.ProtectedFileSystemStorage"
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

# STATIC_ROOT = '/home/taiga/static'
STATIC_URL = f"{ TAIGA_URL }/static/"

#########################################
## EMAIL
#########################################
# https://docs.djangoproject.com/en/3.1/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 120  # seconds

DEFAULT_FROM_EMAIL = 'info@trigonsa.net'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@trigonsa.net'
EMAIL_HOST_PASSWORD = 'Moka@moka7'

#########################################
## EVENTS
#########################################
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": "amqp://taiga:taiga@taiga-events-rabbitmq:5672/taiga"
}


#########################################
## TAIGA ASYNC
#########################################
CELERY_ENABLED = os.getenv('CELERY_ENABLED', 'True') == 'True'

from kombu import Queue  # noqa

CELERY_BROKER_URL = "amqp://taiga:taiga@taiga-async-rabbitmq:5672/taiga"
CELERY_RESULT_BACKEND = None # for a general installation, we don't need to store the results
CELERY_ACCEPT_CONTENT = ['pickle', ]  # Values are 'pickle', 'json', 'msgpack' and 'yaml'
CELERY_TASK_SERIALIZER = "pickle"
CELERY_RESULT_SERIALIZER = "pickle"
CELERY_TIMEZONE = 'Asia/Riyadh'
CELERY_TASK_DEFAULT_QUEUE = 'tasks'
CELERY_QUEUES = (
    Queue('tasks', routing_key='task.#'),
    Queue('transient', routing_key='transient.#', delivery_mode=1)
)
CELERY_TASK_DEFAULT_EXCHANGE = 'tasks'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'task.default'


#########################################
## CONTRIBS
#########################################
# INSTALLED_APPS += [
#     "taiga_contrib_slack",
#     "taiga_contrib_github_auth",
#     "taiga_contrib_gitlab_auth"
# ]
#
# GITHUB_API_CLIENT_ID = "changeme"
# GITHUB_API_CLIENT_SECRET = "changeme"
#
# GITLAB_API_CLIENT_ID = "changeme"
# GITLAB_API_CLIENT_SECRET = "changeme"
# GITLAB_URL = "changeme"


#########################################
## TELEMETRY
#########################################

ENABLE_TELEMETRY = True

#########################################
##  REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = True

#########################################
## THROTTLING
#########################################

#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon-write": "20/min",
#    "user-write": None,
#    "anon-read": None,
#    "user-read": None,
#    "import-mode": None,
#    "import-dump-mode": "1/minute",
#    "create-memberships": None,
#    "login-fail": None,
#    "register-success": None,
#    "user-detail": None,
#    "user-update": None,
#}

# This list should contain:
#  - Taiga users IDs
#  - Valid clients IP addresses (X-Forwarded-For header)
#REST_FRAMEWORK["DEFAULT_THROTTLE_WHITELIST"] = []

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"


#########################################
## STATS
#########################################

#STATS_ENABLED = False
#STATS_CACHE_TIMEOUT = 60*60  # In second


#########################################
## IMPORTERS
#########################################

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
#IMPORTERS["github"] = {
#    "active": True,
#    "client_id": "XXXXXX_get_a_valid_client_id_from_github_XXXXXX",
#    "client_secret": "XXXXXX_get_a_valid_client_secret_from_github_XXXXXX"
#}

# Configuration for the Trello importer
# Remember to enable it in the front client too.
IMPORTERS["trello"] = {
    "active": True, # Enable or disable the importer
    "api_key": "3be725de57354f3838ddff9b7e3c389d",
    "secret_key": "39d79b9b658974b8dffeea62e4d181f3d2a865eac62b6003c65e3e68475e4bd2"
}

# Configuration for the Jira importer
# Remember to enable it in the front client too.
#IMPORTERS["jira"] = {
#    "active": True, # Enable or disable the importer
#    "consumer_key": "XXXXXX_get_a_valid_consumer_key_from_jira_XXXXXX",
#    "cert": "XXXXXX_get_a_valid_cert_from_jira_XXXXXX",
#    "pub_cert": "XXXXXX_get_a_valid_pub_cert_from_jira_XXXXXX"
#}