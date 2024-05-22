"""blueprint for your app views"""
from flask import Blueprint

# Create a blueprint object for your app views
app_views = Blueprint('app_views', __name__)

# pylint disable=C0413
from routes.auth import *
