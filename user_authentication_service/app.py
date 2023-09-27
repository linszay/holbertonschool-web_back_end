#!/usr/bin/env python3
"""setting up basic flask app"""
from flask import Flask, jsonify, request, make_response, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome():
    """use flask.jsonify to return JSON payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    try:
        """try to find user info"""
        email = request.form.get("email")
        password = request.form.get("password")
        """register the new user"""
        new_user = AUTH.register_user(email, password)
        """return JSON payload of the new user"""
        return jsonify({"email": new_user.email,
                        "message": "user created"}), 200
    except ValueError as e:
        """Jreturn SON payload if the user already exists"""
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """get email and pw"""
    email = request.form.get('email')
    password = request.form.get('password')
    """check if the login information is correct"""
    if Auth.valid_login(email, password):
        """create new session and set the session ID as a cookie"""
        session_id = Auth.create_session(email)
        response = make_response(jsonify({"email": email, "message": "logged in"}), 200)
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
