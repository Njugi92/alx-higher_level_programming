#!/usr/bin/python3
""""Print the alphabet in reverse order alternating upper- and lower-case."""
j = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - j)), end="")
    j = 32 if j == 0 else 0
