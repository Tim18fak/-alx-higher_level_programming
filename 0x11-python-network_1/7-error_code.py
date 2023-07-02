#!/usr/bin/python3
"""Sends a request to a given URL.
Displays the response body.
Usage: python3 7-error_code.py <URL>
  - Handles HTTP errors.
"""
import requests
import sys


if __name__ == "__main__":
    link = sys.argv[1]

    fetch= requests.get(link)
    if fetch.status_code >= 400:
        print("Error code: {}".format(fetch.status_code))
    else:
        print(fetch.text)
