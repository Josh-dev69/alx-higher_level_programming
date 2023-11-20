#!/usr/bin/python3
""" A Script that lists all states from
    the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()

    # Execute the SQL Query
    query = "SELECT * FROM states"
    cursor.execute(query)

    # Fetch and Display the Results
    results = cursor.fetchall()
    for row in results:
        print(row)
