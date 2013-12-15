import os

DJANGO_STARTUP_APP_KEY = "DJANGO_STARTUP_APP_LIST"


def get_environmental_start_apps():
    val = os.environ.get(DJANGO_STARTUP_APP_KEY, None)
    if val is not None and val is not "":
        return tuple([e for e in val.split(" ")])
    return None