from blog.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q0a1y9@+j)ay_+l4fs7j94pwl6b&0n*^%)!m0&l+we=$u4ih=7'

if env('DEBUG') == 'TRUE':
    DEBUG = True
elif env('DEBUG') == 'FALSE':
    DEBUG = False