#!/usr/bin/python3
"""Outputs value of X-Request-Id variable found in
header of response.
"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    value = {"email": argv[2]}
    request = Request(
            argv[1], urlencode(value).encode("ascii"))
    with urlopen(request) as response:
        head = response.headers.get('X-Request-Id')
        print(response.read().decode('utf-8'))
