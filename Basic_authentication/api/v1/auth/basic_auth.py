#!/usr/bin/env python3
"""new class inherits from Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """New class inherits from Auth"""
    def __init__(self):
        pass

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """returns Base64 part of authorization header"""
        authH = authorization_header
        if authH is None or not isinstance(authH, str) \
                or not authH.startswith('Basic '):
            return None
        """split auth header after ' ' to only return Base64"""
        return authH.split(' ')[1]
