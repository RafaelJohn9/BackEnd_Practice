"""Contains auth routes"""
from datetime import timedelta
from flask import request, jsonify, current_app
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended.utils import get_jti, get_jwt, get_jwt_identity
from redis import Redis
from utils.jwt_helpers import store_jwt
from models import db, User
from routes import app_views


@app_views.route('/register', methods=['POST'])
def register():
    """ registers a new user"""
    # Get the user data from the request
    data = request.get_json()

    # Extract the username and password from the data
    username = data.get('username')
    password = data.get('password')

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # Return a response
    return jsonify({'message': 'User registered successfully'})

@app_views.route('/login', methods=['POST'])
def login():
    """ logs in a user"""
    data = request.get_json()

    # Extract the username and password from the data
    username = data.get('username')
    password = data.get('password')

    # Query the database to get the user with the given username
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'invalid credentials'}), 401

    # Generate the JWT access token
    access_token = create_access_token(identity=user.id)
    jti = get_jti(encoded_token=access_token)
    redis_client = Redis.from_url(current_app.config['REDIS_URL'])
    store_jwt(
              redis_client=redis_client,
              jwt_token=jti,
              user_id=user.id,
              time=timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
              )

    # Return the access token in the response
    return jsonify({
                    'message': 'User logged in successfully',
                    'access_token': access_token.decode('utf-8')
                    })

@app_views.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """used to log out a user"""
    jti = get_jwt()["jti"]
    redis_client = Redis.from_url(current_app.config['REDIS_URL'])
    redis_client.delete(jti)
    return jsonify({"msg": "Successfully logged out"}), 200

@app_views.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """Protected route that requires JWT authentication"""
    return jsonify({'message': 'Protected route accessed by user:'})

@app_views.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """used to refresh the JWT token"""
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)
    redis_client = Redis.from_url(current_app.config['REDIS_URL'])
    jti = get_jti(encoded_token=access_token)
    store_jwt(redis_client, jti, user_id, timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES']))
    return jsonify(access_token=access_token), 200
