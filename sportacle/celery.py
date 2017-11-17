import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportacle.settings')

app = Celery('sportacle')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()