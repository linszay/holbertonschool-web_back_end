#!/usr/bin/env python3
"""new class inherits from Auth"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """new class inherits from Auth"""
    def __init__(self):
        pass

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method creates a session id for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        """generates a universally unique identifier"""
        session_id = str(uuid.uuid4())
        """assigning key (session_id) to value (user_id)"""
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method returns user_id for session_id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        """getting the value for session_id key"""
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """(overload) returns user instance based on cookie value"""
        """session cookie req to get session_id"""
        session_id = self.session_cookie(request)
        """get user instance based on session"""
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """deletes user session / logout"""
        if request is None:
            return False
        """request session id"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        """return false if session id doesn't have a user"""
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        """finally delete session id and return true"""
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True
