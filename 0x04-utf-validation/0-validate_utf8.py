#!/usr/bin/python3
"""
Utf-8 validation
"""


def validUTF8(data):
    """
    Checks if intergers in a list are all valid
    UTF-8 encoding
    """
    for i in data:
        if i > 255:
            return False
    return True
