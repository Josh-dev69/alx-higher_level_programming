#!/usr/bin/python3
""" A Script that takes an argument and match it with
    the values in the 'states' table of the
    database 'hbtn_0e_0_usa' """

import MySQLdb
import sys

if __name__ == "__main__":
    # Set up connection
    conn = MySQLdb.connect(
            user = sys.argv[1],
            passwd = sys.argv[2],
            db = sys.argv[3]
        )
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name = %s \
            ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    results = cursor.fetchall()
    for row in results:
        print(row)
