#!/usr/bin/python3

""" a script that lists all State objects
from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City, Base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
