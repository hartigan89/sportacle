"""
WSGI config for sportacle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from django.core.exceptions import ImproperlyConfigured
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# Handling Key Import Errors
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Get ENV VARIABLES key
ENV_ROLE = get_env_variable('ENV_ROLE')

if ENV_ROLE == 'production':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.prod")
elif ENV_ROLE == 'development':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.dev")
elif ENV_ROLE == 'c9':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.c9")

application = Cling(get_wsgi_application())
