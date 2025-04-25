from .common import *
import os
SECRET_KEY = 'django-insecure-ldhd93z0f@kdztxioary-2sh49gv!!6vgf*2@13c-e)=d_qps7'

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
