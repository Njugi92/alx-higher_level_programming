#!/usr/bin/python3
"""script that takes in a URL, sends a request to
URL and displays value of variable X-Request-Id in
response header
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    html = get(argv[1])
    print(html.headers.get('X-Request-Id'))
