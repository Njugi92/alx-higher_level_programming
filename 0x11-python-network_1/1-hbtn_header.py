#!/usr/bin/python3
"""Outputs value of X-Request-Id variable found in
the header of response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
