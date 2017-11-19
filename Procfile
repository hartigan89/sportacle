web: python manage.py collectstatic --noinput; gunicorn sportacle.wsgi
worker: celery -A tasks worker --loglevel=info
beat: celery -A sportacle beat