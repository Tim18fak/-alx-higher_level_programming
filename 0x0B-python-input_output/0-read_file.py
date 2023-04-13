#!/usr/bin/python
"""
read_file function
"""


def read_file(fil=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(fil, "r", encoding="utf-8") as f:
        print(f.read(), end="")
