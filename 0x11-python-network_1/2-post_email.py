#!/usr/bin/python3

"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the responses body
        body = response.read().decode('utf-8')
        print(body)
