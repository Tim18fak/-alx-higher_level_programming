#!/usr/bin/python3
"""retrieve  https://alx-intranet.hbtn.io/status using requests modules"""
import requests
if __name__ == "__main__":
    fetch = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(fetch.text)))
    print("\t- content: {}".format(fetch.text))
