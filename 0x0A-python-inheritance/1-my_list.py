#!/usr/bin/python3
"""
the MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initialization  happens"""
        super().__init__()

    def print_sorted(self):
        """prints the ist"""
        print(sorted(self))
