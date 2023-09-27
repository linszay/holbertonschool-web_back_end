#!/usr/bin/env python3
"""define _hash_password method"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
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

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the email and password are valid for login."""
        try:
            """try to find the user by email"""
            user = self._db.find_user_by(email=email)
            """check if pw matches by using bcrypt.checkpw"""
            if bcrypt.checkpw(password.encode('utf-8'),
                              user.hashed_password):
                return True
            else:
                return False
        except Exception as e:
            return False

def _generate_uuid() -> str:
    """returns str representation of new UUID"""
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hash as bytes."""
    """create a salt"""
    salt = bcrypt.gensalt()
    """use the salt to make a salted hash & return it"""
    return bcrypt.hashpw(password.encode('utf-8'), salt)
