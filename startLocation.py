#!/usr/bin/env python
import os
import sys
from registry.client import RegistryClient

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    # Import Core Settings Module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "location.settings")

    name = "location1"

    registry_client = RegistryClient()
    port = registry_client.register(name)

    # Add Arguments for StartUp
    sys.argv = ["manage.py", "runserver", "localhost:%i" % port]

    # Start it
    execute_from_command_line(sys.argv)
