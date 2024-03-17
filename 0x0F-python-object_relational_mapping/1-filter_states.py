#!/usr/bin/python3

"""
a script that lists all states with a name starting with N
script should take 3 arguments:
mysql username, mysql password and database name
script should connect to a MySQL server running on localhost at port 3306
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()

    filter_by = 'N%'

    cur.execute("""SELECT *
            FROM states WHERE name LIKE %s
            ORDER BY id ASC""", (filter_by,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
