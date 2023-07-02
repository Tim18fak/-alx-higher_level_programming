#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: python3 6-post_email.py <URL> <email>
  - show the body of the response.
"""
import requests
import sys



if __name__ == "__main__":
    link = sys.argv[1]
    email = {"email": sys.argv[2]}

    r = requests.post(link, data=email)
    print(fetch.text)
