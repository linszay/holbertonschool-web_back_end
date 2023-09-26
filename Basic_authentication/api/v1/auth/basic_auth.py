#!/usr/bin/env python3
"""new class inherits from Auth"""
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)\
            -> (str, str):
        """returns user email and pw from decoded base64 value"""
        decoded = decoded_base64_authorization_header
        colon = ':'
        if decoded is None or not isinstance(decoded, str) \
                or colon not in decoded:
            return None, None
        return decoded.split(':')

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) \
            -> TypeVar('User'):
        """returns User instance from email and pw"""
        if user_email is None or not isinstance(user_email, str) \
                or user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            """using search to check db for matching email"""
            email_found = User.search({'email': user_email})
            if not email_found:
                return None
            """if found then assign 1st matching item to user"""
            user = email_found[0]
            """if no pw or wrong pw then return None"""
            if not user.is_valid_password(user_pwd):
                return None
        except Exception:
            return None
        """else return user instance"""
        return user
