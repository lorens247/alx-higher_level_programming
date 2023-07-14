#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {password}'}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        print(data['id'])
    else:
        print("None")
