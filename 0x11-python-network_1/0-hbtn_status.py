#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request


if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    request = urllib.request.Request(link)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}" + str(type(body)))
        print("\t- content: {}" + str(body))
        print("\t- utf8 content: {}" + str(body.decode("utf-8")))
