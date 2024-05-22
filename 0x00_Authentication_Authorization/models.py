"""
A simple User model
"""
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """
    User model
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), default='user')

    def set_password(self, password):
        """used to set the password of the user"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """used to check the password of the user"""
        return check_password_hash(self.password_hash, password)
