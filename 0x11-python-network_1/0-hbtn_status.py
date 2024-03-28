#!/usr/bin/python3
"""  a Python script that fetches
https://alx-intranet.hbtn.io/status """

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html_content = response.read().decode('utf-8')


print("Body response:")
print("\t- type: {}".format(type(html_content)))
print("\t- content: {}".format(html_content))
