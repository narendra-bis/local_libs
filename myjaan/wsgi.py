"""
WSGI config for myjaan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myjaan.settings")
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldname.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'local_lib.settings')

application = get_wsgi_application()
