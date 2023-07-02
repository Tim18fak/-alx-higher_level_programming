#!/usr/bin/python3
# Fetches https://alx-intranet.hbtn.io/status
import urllib.request

link = "https:/alx-intranet.btn.io/status"

if __name__ == "__main__":
    request = urllib.request.Request(link)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: %s" % type(body))
        print("\t- content: " + str(body))
        print("\t- utf8 content: " + body.decode("utf-8"))
