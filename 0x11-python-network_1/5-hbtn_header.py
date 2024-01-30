#!/usr/bin/python3
""" Script that takes in a URL """
import sys
import requests

if __name__ == "__main__":
    """ Packages """
    url_data = sys.argv[1]
    b = requests.get(url_data)
    print(b.headers.get("X-Request-Id"))
