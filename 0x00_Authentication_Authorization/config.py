""" Contains the configuration for the application """

import os
class Config:
    """
    Contains the configuration for the application
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious_secret_key')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt_secret')
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
