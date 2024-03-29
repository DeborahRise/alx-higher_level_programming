#!/usr/bin/python3

"""
a script that lists all states with a name starting with N
script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()

    filter_by = 'N%'

    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
            ORDER BY id ASC""", (filter_by,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
