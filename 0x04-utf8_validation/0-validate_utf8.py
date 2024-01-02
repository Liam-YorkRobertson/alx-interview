#!/usr/bin/python3
"""
UTF-8 validation function
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    try:
        bytes(data).decode("UTF-8", errors="strict")
        return True
    except (UnicodeDecodeError, ValueError):
        return False
