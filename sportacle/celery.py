from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportacle.settings')

app = Celery('sportacle')
app.config_from_object('celeryconfig')
app.autodiscover_tasks()