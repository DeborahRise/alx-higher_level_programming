#!/usr/bin/python3

"""
a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    # Check if HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f'Error code: {response.status_code}')
    else:
        # Display the body of the response
        print(response.text)
