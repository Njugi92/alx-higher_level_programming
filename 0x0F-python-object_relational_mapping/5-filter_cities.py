#!/usr/bin/python3
"""
The script that takes name of the state as an arg
and lists all cities of thaat state ausing database
"""
import MySQLdb
from sys import argv

# Should not be executed when imported
if __name__ == '__main__':
    # Establish a connection to database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rows = cur.fetchall()
    j = []
    for k in rows:
        j.append(k[1])
    print(", ".join(j))

    cur.close()
    db.close()
