#!/usr/bin/env python
import os
import sys

from testrpc.settings_helper import DJANGO_STARTUP_APP_KEY

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    # Import Core Settings Module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testrpc.settings")

    # Define Apps to Start With this "Server"
    os.environ.setdefault(DJANGO_STARTUP_APP_KEY, "registry")

    # Add Arguments for StartUp
    sys.argv = ["manage.py", "runserver", "localhost:5555"]

    # Start it
    execute_from_command_line(sys.argv)
