import os

broker_url = os.environ.get('CLOUDAMQP_URL')
broker_pool_limit = 1 # Will decrease connection usage
broker_heartbeat = None # We're using TCP keep-alive instead
broker_connection_timeout = 30 # May require a long timeout due to Linux DNS timeouts etc
result_backend = None # AMQP is not recommended as result backend as it creates thousands of queues
event_queue_expires = 60 # Will delete all celeryev. queues without consumers after 1 minute.

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'