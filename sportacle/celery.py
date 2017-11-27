from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from sportacle.settings.base import get_env_variable

# Get ENV VARIABLES key
ENV_ROLE = get_env_variable('ENV_ROLE')

if ENV_ROLE == 'production':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.prod")
elif ENV_ROLE == 'development':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.dev")
elif ENV_ROLE == 'c9':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.c9")

app = Celery('sportacle')
app.config_from_object('celeryconfig')
app.autodiscover_tasks()