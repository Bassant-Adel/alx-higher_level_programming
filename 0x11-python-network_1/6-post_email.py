#!/usr/bin/python3
""" script that takes in a URL """
import sys
import requests

if __name__ == "__main__":
    """ email """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
