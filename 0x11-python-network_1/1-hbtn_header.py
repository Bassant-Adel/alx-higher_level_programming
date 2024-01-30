#!/usr/bin/python3
""" Write to take in URL """
import sys
import urllib.request

if __name__ == "__main__":
    """ X-Request-Id """
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
