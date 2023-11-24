#!/usr/bin/python3
"""
    A script that lists all State objects from the database
    hbtn_0e_6_usa using ORM
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get MySQL connection parameters from command line arguments
    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    
    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(user, pwd, db), pool_pre_ping=True)

    # Create a configured session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query to fetch all states
    states = session.query(State).order_by(State.id).all()

    # Looping and displaying the fetched query 
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
