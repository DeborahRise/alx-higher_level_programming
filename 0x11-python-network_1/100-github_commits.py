#!/usr/bin/python3

"""
a Python script that takes 2 arguments in order to solve this challenge.
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Github endpoint for user info
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repo_name)

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')
                ))
    except IndexError:
        pass
