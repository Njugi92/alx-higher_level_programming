#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    totals = 0
    for k in range(len(sys.argv) - 1):
        totals += int(sys.argv[k + 1])
    print("{}".format(totals))
