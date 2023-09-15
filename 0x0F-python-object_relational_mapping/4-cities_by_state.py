#!/usr/bin/python3
"""
The script that lists all cities from the
database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

# code should not be executed when imported
if __name__ = '__main__':
    # Establishing connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for k in rows:
        print(k)
    cur.close()
    db.close()