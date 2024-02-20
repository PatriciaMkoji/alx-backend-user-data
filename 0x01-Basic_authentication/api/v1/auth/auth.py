#!/usr/bin/env python3
""" Manage the API Authentication """
from flask import request
from typing import List, TypeVar


class Auth():
    """ a class that manages Api Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False-path & excluded-paths """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        # make sure excluded_paths ends with '/'
        excluded_paths = [p if p.endswith('/')
                          else p + '/' for p in excluded_paths]

        # Add a trailing slash to path for comparison
        path = path if path.endswith('/') else '/'

        # check if the path is in excluded_paths
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Will be the Flask request object """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ request will be the Flask request object """
        return None
