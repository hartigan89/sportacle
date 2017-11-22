web: python manage.py collectstatic --noinput; gunicorn sportacle.wsgi
worker: celery -A sportacle worker --loglevel=info --without-gossip --without-mingle --without-heartbeat
beat: celery -A sportacle beat --without-gossip --without-mingle --without-heartbeat