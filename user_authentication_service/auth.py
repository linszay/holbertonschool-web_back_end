#!/usr/bin/env python3
"""define _hash_password method"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hash as bytes."""
    """create a salt"""
    salt = bcrypt.gensalt()
    """use the salt to make a salted hash & return it"""
    return bcrypt.hashpw(password.encode('utf-8'), salt)
