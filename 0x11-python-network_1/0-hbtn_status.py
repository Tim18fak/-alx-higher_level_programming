#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    request = urllib.request.Request(link)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:")
        print(type(body))
        print("\t- content:")
        print(body)
        print("\t- utf8 content:")
        print(body.decode("utf-8"))
