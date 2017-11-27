#!/usr/bin/env python
import os
import sys
from sportacle.settings.base import get_env_variable

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
