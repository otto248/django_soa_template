#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line


def test_service_app(name):
     # Import Core Settings Module
    os.environ["DJANGO_SETTINGS_MODULE"] = "%s.settings" % name
    args = ["", "test", name]
    execute_from_command_line(args)


if __name__ == "__main__":
    test_service_app(sys.argv[1])

