#!/usr/bin/env python3
"""new class inherits from Auth"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """returns the decoded base64 part of auth header"""
        base = base64_authorization_header
        if base is None or not isinstance(base, str):
            return None
        try:
            decoded = base64.b64decode(base)
            result = decoded.decode('utf-8')
            return result
        except Exception:
            return None
