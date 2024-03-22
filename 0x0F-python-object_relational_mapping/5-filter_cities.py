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
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()
    state_name = sys.argv[4]

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    result = ", ".join(cities)
    print(result)

    cur.close()
    db.close()
