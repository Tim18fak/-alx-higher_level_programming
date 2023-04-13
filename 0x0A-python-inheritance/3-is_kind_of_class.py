#!/usr/bin/python3
"""
Contains the is_kind_of_class function
"""


def is_kind_of_class(name, class_name):
    if type(name) == class_name:
        return True
    else:
        for sal in class_name.__mro__[1:]:
            if isinstance(name, sal):
                return True
        return False
