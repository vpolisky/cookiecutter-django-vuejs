"""
WSGI config for {{cookiecutter.project_name}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_name}}.settings')

application = WhiteNoise(get_wsgi_application())
application.add_files(os.path.join(settings.BASE_DIR, 'static'), prefix='static')
application.add_files(os.path.join(settings.BASE_DIR, 'webapp', 'dist'), prefix='')

