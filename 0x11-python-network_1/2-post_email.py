#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    link = sys.argv[1]
    email = {"email": sys.argv[2]}
    message = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(link, message)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
