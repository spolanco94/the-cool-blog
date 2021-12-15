from blog.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

if env('DEBUG') == 'TRUE':
    DEBUG = True
elif env('DEBUG') == 'FALSE':
    DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']