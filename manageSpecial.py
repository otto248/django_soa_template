#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    args = sys.argv
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % args[-1])
    args = args[0:len(args)-1]

    execute_from_command_line(args)
