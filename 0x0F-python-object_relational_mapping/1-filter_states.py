#!/usr/bin/python3
""" A Script that lists all states with a name
    starting with N (upper N) from the 
    database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    # Set up connection
    conn = MySQLdb.connect(
            user = sys.argv[1],
            passwd = sys.argv[2],
            db = sys.argv[3]
        )
    cursor = conn.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        if row[1][0] == 'N':
            print(row)
    
    cursor.close()
    conn.close()
