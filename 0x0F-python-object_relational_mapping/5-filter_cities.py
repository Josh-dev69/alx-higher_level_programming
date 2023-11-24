#!/usr/bin/python3
"""
    A script that lists all cities from the database 
    hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id ASC"

    cur.execute(query, (argv[4], ))
    result = cur.fetchall()
    if result is not None:
        print(", ".join([row[0] for row in result]))
    cur.close()
    conn.close()
