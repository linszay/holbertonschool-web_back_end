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

    def create_session(self, email: str) -> str:
        """create a session for the user and return the session ID"""
        try:
            """find the user by email"""
            user = self._db.find_user_by(email=email)
            """create a new session ID"""
            session_id = str(uuid.uuid4())
            """update the users session_id in the db"""
            user.session_id = session_id
            """commit changes to db"""
            self._db._session.commit()
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """takes session_id and returns User or None"""
        if session_id is None or not session_id:
            return None
        try:
            """try to find user"""
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """takes user_id and returns none"""
        """find user by user_id"""
        user = self._db.find_user_by(id=user_id)
        if user:
            """remove session_id"""
            user.session_id = None
            """commit changes to db"""
            self._db.commit()
        return None


def _generate_uuid() -> str:
    """returns str representation of new UUID"""
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hash as bytes."""
    """create a salt"""
    salt = bcrypt.gensalt()
    """use the salt to make a salted hash & return it"""
    return bcrypt.hashpw(password.encode('utf-8'), salt)
