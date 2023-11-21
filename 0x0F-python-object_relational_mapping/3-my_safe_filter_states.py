#!/usr/bin/python3
""" 

A Script that takes an argument and match it with
the values in the 'states' table of the
database 'hbtn_0e_0_usa' 

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s \
            ORDER BY id ASC"
    cur.execute(query, (argv[4], ))

    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
