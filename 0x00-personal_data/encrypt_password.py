#!/usr/bin/env python3
"""Defines and return a hash_password function."""
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """Returns a hashed password."""
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a password is valid or return boolean."""
    return bcrypt.checkpw(password.encode(), hashed_password)
