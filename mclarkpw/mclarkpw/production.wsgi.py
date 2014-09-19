"""
WSGI config for mclarkpw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys

virtualenv_dir = os.environ["VIRTUALENV_DIR"]

# Activate your virtual env
activate_env=os.path.join(virtualenv_dir,"/mclarkpw/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mclarkpw.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
