"""
WSGI config for iskcongkp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if "ENVIRONMENT_NAME" in os.environ:
    environment_name = os.environ['ENVIRONMENT_NAME']
    environment_settings_file = "iskcongkp.settings."+environment_name
else:
    environment_settings_file = "iskcongkp.settings.dev"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", environment_settings_file)

application = get_wsgi_application()
