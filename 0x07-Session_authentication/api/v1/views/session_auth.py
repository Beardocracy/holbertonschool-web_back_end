#!/usr/bin/env python3
''' This module contains session_auth routes '''
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    '''
    POST /auth_session/login
    Return: User instance
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    if not email:
        return jsonify({"error": "email missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        ret = jsonify(user.to_json())
        ret.set_cookie(getenv('SESSION_NAME'), session_id)
        return ret
    return jsonify({"error": "no user found for this email"}), 404
