#!/usr/bin/env python3
"""new class inherits from Auth"""
from api.v1.auth.auth import Auth
import uuid


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
        user_id = SessionAuth.user_id_by_session_id.get(session_id)
        return user_id
