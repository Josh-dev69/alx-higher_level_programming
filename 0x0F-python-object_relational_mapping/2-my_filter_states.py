#!/usr/bin/python3
""" 

A Script that takes an argument and match it with
the values in the 'states' table of the
database 'hbtn_0e_0_usa' 

"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3]
    )
    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY'{}' \
            ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    conn.close()
