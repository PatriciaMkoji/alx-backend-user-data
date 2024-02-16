#!/usr/bin/env python3
""" Manage the API Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ a class that manages Api Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False-path & excluded-paths """
        return False

    def authorization_header(self, request=None) -> str:
        """ Will be the Flask request object """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ request will be the Flask request object """
        return None
