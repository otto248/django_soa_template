#!/usr/bin/env python
import os
import sys

from testrpc.settings_helper import DJANGO_STARTUP_APP_KEY

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testrpc.settings")
    os.environ.setdefault(DJANGO_STARTUP_APP_KEY, "payment location")

    from django.core.management import execute_from_command_line

    print sys.argv

    execute_from_command_line(sys.argv)
