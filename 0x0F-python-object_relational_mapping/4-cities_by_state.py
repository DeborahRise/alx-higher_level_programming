#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_0_usa
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

    query = """
        SELECT * FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
