import os
import sys

path = '/srv/django'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'appsec.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
