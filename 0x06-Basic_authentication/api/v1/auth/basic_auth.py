#!/usr/bin/env python3
'''
This module contains Basic Auth
'''
import base64
from api.v1.auth.auth import Auth


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
