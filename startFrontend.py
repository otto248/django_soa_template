#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    # Import Core Settings Module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frontend.settings")

    # Add Arguments for StartUp
    args = ["startFrontend.py", "runserver", "localhost:%i" % 8000]

    # Start it
    execute_from_command_line(args)
