#!/usr/bin/python3
""" 
A Script that lists all states with N (upper N) 
from the states table

"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE \
            BINARY'N%' ORDER BY id ASC")

    results = cur.fetchall()
    for row in results:
        print(row)
    
    cur.close()
    conn.close()
