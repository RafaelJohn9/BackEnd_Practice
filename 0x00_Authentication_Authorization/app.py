#!/usr/bin/env python3
"""Application entry point."""
from flask import Flask
from flask_jwt_extended import JWTManager
from redis import Redis
from config import Config
from utils.jwt_helpers import is_token_revoked
from routes import app_views
from models import db

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
redis_client = Redis.from_url(app.config['REDIS_URL'])

@app.route('/')
def home():
    return 'Welcome to the home page!'

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_payload):
    """Checks if the JWT token is revoked"""
    jti = jwt_payload['jti']
    return is_token_revoked(redis_client, jti)

app.register_blueprint(app_views)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
