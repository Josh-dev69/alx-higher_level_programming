#!/usr/bin/python3
""" 
A Script that lists all states with N (upper N) 
from the database hbtn_0e_0_usa

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
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE \
            BINARY'N%' ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)
    
    cursor.close()
    conn.close()
