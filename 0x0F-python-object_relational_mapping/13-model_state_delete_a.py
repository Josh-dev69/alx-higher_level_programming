#!/usr/bin/python3
"""
    A script that deletes a record from the database using ORM

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and deleting a state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    search_query = session.query(State).filter(
        State.name.like('%a%')).all()

    for state_name in search_query:
        session.delete(state_name)
    session.commit()
    session.close()
