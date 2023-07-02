#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    fetch = urllib.request.Request(url)
    link = sys.argv[1]
    try:
        with urllib.request.urlopen(fetch) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
