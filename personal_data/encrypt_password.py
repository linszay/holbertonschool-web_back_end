#!/usr/bin/env python3
"""takes string and returns salted, hashed password as byte string"""
import bcrypt

def hash_password(password: str) -> bytes:
    """returns password as byte string"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
