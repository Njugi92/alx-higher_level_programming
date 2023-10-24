#!/usr/bin/python3
"""
The script that lists all states with a name
starting with N (upper N) from database
"""
import MySQLdb
from sys import argv

# code should not be excecuted when imported
if __name__ == '__main__':
    # Establish database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # This enables ability for multiple separate working
    # environment through the same connection to database
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for k in rows:
        print(k)
    # The clean up process
    cur.close()
    db.close()
