#!/usr/bin/env python3
"""new flask view handles routes for session auth"""
from api.v1.views import app_views
from flask import jsonify, request, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """handles all routes for session authentication"""
    paths = ['/auth_session/login', '/auth_session/login/']
    """use request.form.get to retrieve email and pw"""
    email = request.form.get('email')
    password = request.form.get('password')
    """if email or pw missing/empty return json and status code"""
    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400
    """use User.search to retrieve user instance from email"""
    user = User.search({'email': email})
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404
    """if no pw or wrong pw then return None"""
    if not user[0].is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    """create session id for user id"""
    """import in route/method to avoid circular import"""
    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    """using getenv to get our session_name env variable"""
    session_name = os.getenv('SESSION_NAME')
    """use to_json to return dict rep of the user"""
    """set the cookie to the response"""
    resp = make_response(user[0].id.tojson())
    resp.set_cookie(session_name, session_id)
    return resp
