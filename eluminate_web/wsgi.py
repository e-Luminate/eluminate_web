"""
WSGI config for eluminate_web project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eluminate_web.settings")

### now do special stuff for the production server, if local_wsgi.py exists
## disabled and replaced by more straightforward version below
#try:
#    execfile("eluminate_web/local_wsgi.py")
#except IOError:
#    pass

# try to activate virtualenv (may be needed on production server; judging by today's effort, it is!)
activate_this = os.path.expanduser("~/.virtualenvs/eluminate_env/bin/activate_this.py")
try:
    execfile(activate_this, dict(__file__=activate_this))
except:
    pass

import eluminate_web.startup as startup
startup.run()

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
