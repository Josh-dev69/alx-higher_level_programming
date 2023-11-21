#!/usr/bin/python3
"""
A Script that lists name of states in the states table
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    conn.close()
