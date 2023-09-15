#!/usr/bin/python3
"""
The script that takes in an argument and display
all values in the state table of hbtn_0e_0_usa
where name matches the argument but safe from
MySQL injection
"""
import MySQLdb
from sys import argv

# Code should not be executed when imported
if __name__ = '__main__':
    # Start a connection to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # For ability to have multiple working environments
    # via the same connection to the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for k in rows:
        print(k)
    # clean up process
    cur.close()
    db.close()
