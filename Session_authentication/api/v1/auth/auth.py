#!/usr/bin/env python3
"""create a class to manage API authentication"""
import flask
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """new class for auth management"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false for now - path & excluded_paths used later"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        else:
            for character in excluded_paths:
                character = character.replace('/', '')
                path = path.replace('/', '')
                if path == character:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be Flask req object"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be Flask req object"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        """get value of cookie my_session_id from env var session_name"""
        sesssion = os.getenv('SESSION_NAME', '_my_session_id')
        """using request to access the cookie from req cookie dict"""
        cookie = request.cookies.get(sesssion)
        return cookie
