#!/usr/bin/env python
import os
import sys
from django.core.exceptions import ImproperlyConfigured

# Handling Key Import Errors
def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

if __name__ == "__main__":
    # Get ENV VARIABLES key
    ENV_ROLE = get_env_variable('ENV_ROLE')

    if ENV_ROLE == 'production':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.prod")
    elif ENV_ROLE == 'development':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.dev")
    elif ENV_ROLE == 'c9':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportacle.settings.c9")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
