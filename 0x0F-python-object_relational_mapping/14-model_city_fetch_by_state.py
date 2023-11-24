#!/usr/bin/python3
"""
    A script that joins state and cities object in database using ORM

"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and joining the state
    and cities
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State)

    for city, state in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
