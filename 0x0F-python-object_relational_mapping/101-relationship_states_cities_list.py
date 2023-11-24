#!/usr/bin/python3
"""
    A script that list all State object and corresponding City object
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for row in query:
        print("{}: {}".format(row.id, row.name))
        for city_instance in row.cities:
            print("    {}: {}".format(city_instance.id, city_instance.name))
