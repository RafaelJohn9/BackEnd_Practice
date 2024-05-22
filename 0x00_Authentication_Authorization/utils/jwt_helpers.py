""" This module contains helper functions for working with JWT tokens."""
import json
from redis import Redis

def store_jwt(redis_client: Redis, jwt_token: str, user_id: int, time) -> None:
    """Stores the JWT token in Redis"""
    redis_client.setex(jwt_token, time, json.dumps({'user_id': user_id}))

def is_token_revoked(redis_client: Redis, jti: str) -> bool:
    """Checks if the JWT token is revoked"""
    return redis_client.get[jti] is None
