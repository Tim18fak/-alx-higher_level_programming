#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, class_type):
    """return true if obj is the exact class class_type, otherwise false"""
    return (type(obj) == class_type)
