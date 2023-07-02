#!/usr/bin/python3
"""Displays the X-Request-Id header variable
Usage: python3 5-hbtn_header.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    link = sys.argv[1]

    fetch = requests.get(link)
    print(r.headers.get("X-Request-Id"))
