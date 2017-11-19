web: python manage.py collectstatic --noinput; gunicorn sportacle.wsgi
worker: celery -A sportacle worker --loglevel=info
beat: celery -A sportacle beat