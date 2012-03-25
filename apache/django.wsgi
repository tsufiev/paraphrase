import os
import sys

path = ['/home/dev/web', 
        '/home/dev/.virtualenvs/paraphrase/lib/python2.6/site-packages']
sys.path.extend(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'paraphrase.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
