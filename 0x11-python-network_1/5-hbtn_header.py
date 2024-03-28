#!/usr/bin/python3

"""
a Python script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found
in the header of the response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)
    # Check if 'X-Request-Id is present in the responseheader
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print(request_id)
