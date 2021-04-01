#!/usr/bin/env python3
'''
This module contains Basic Auth
'''
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    ''' Basic Auth '''
    def __init__(self):
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        ''' Does what it says '''
        h = authorization_header
        if not h or not isinstance(h, str) or not h.startswith("Basic "):
            return
        return h[6:]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        ''' Docstring '''
        if not user_email or not user_pwd:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            from models.user import User
            user = User.search({"email": user_email})
        except Exception:
            return None
        if not user:
            return None
        if user[0].is_valid_password(user_pwd):
            return user[0]
        else:
            return None
