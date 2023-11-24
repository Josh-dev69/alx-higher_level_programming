#!/usr/bin/python3
"""
    A script that lists all cities from the
    database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

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
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id ASC"
    cur.execute(query, (argv[4], ))
    result = cur.fetchall()
    if result is not None:
        result_strings = []
        for row in result:
            result_strings.append(str(row[0]))

    result_string = ", ".join(result_strings)
    print(result_string)

    cur.close()
    conn.close()
