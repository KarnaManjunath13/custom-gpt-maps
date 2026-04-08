# config.py

import os

# Flask configuration
class Config:
    DEBUG = os.environ.get('FLASK_DEBUG') == '1'
    TESTING = os.environ.get('FLASK_TESTING') == '1'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# API Keys
API_KEY_SERVICE_1 = os.environ.get('API_KEY_SERVICE_1')
API_KEY_SERVICE_2 = os.environ.get('API_KEY_SERVICE_2')

