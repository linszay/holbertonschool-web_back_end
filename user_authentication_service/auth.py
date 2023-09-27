#!/usr/bin/env python3
"""define _hash_password method"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        # sourcery skip: use-contextlib-suppress, use-named-expression
        """takes email and pw and returns a user object"""
        """check if email already in use"""
        try:
            current_user = self._db.find_user_by(email=email)
            if current_user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            pass
        """hash the password"""
        hashed_password = _hash_password(password)
        """create new user w email and pw & return user"""
        return self._db.add_user(email=email, hashed_password=hashed_password)


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hash as bytes."""
    """create a salt"""
    salt = bcrypt.gensalt()
    """use the salt to make a salted hash & return it"""
    return bcrypt.hashpw(password.encode('utf-8'), salt)
