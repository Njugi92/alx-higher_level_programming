#!/usr/bin/python3
"""
The script that takes an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
from sys import argv

# Code should not be executed when imported
if __name__ = '__main__':
    # Establish a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # In order to have multiple separate working environment
    # via same connection
    cur = db.cursor()
    nameSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nameSr)

    rows = cur.fetchall()
    for k in rows:
        print(k)
    # The clean up process
    cur.close()
    db.close()
