"""
WSGI config for mclarkpw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys


# Activate your virtual env
activate_env="/var/envs/mclarkpw/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mclarkpw.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
