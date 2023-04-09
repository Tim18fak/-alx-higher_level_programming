#!/usr/bin/python3
"""
This is the "0-add integer" moduledef add_integer(a, b):
"""


def add_integer(a, b):
    """    Return the addition of two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float) or isinstance(a, float):
        b = int(b)
        a = int(a)
    return a + b
