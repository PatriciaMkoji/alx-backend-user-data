#!/usr/bin/env python3
""" Password Encryption & Validation Module """
import bcrypt


def hash_password(password):
    """ Generates a salted & Hashed Password """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
