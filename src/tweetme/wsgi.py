"""
WSGI config for tweetme project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweetme.settings")

application = get_wsgi_application()


# for heroku
# import os
# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tweetme.settings")
# application = Cling(get_wsgi_application())




# from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

# application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
