#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
"""Load the correct auth based on the AUTH_TYPE env variable"""
auth_type = os.getenv("AUTH_TYPE")
if auth_type == "auth":
    auth = Auth()
elif auth_type == "basic_auth":
    auth = BasicAuth()


@app.before_request
def before_request():
    """Before request"""
    if auth is None:
        return

    """Paths that don't require authentication"""
    excluded_paths = ['/api/v1/status/', '/api/v1/status',
                      '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if request.path not in excluded_paths:
        if auth.authorization_header(request) is None:
            abort(401)

        if auth.current_user(request) is None:
            abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized request"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden request"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
