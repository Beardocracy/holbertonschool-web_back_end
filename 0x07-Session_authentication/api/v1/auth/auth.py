#!/usr/bin/env python3
'''
This module contains the Auth class
'''
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    '''
    Auth class docs
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Check if a path requires authorization '''
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or (path + '/') in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' authorization_header docs '''
        if request and 'Authorization' in request.headers:
            return request.headers.get('Authorization')
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' current_user docs '''
        return None

    def session_cookie(self, request=None):
        ''' Retruns a cookie value from a request '''
        if request:
            return request.cookies.get(getenv('SESSION_NAME'))
