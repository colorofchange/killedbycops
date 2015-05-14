"""
WSGI config for killedbycops project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "killedbycops.settings")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'mediafiles'))  # DRY, get this from django settings?
print "loading waitress"
print "BASE_DIR", BASE_DIR
print "MEDIA_ROOT", MEDIA_ROOT

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
application.add_files(MEDIA_ROOT, prefix='media/')
