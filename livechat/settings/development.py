from .base import *

with open('secret_key.txt', 'rt') as secret:
    SECRET_KEY = secret.read()