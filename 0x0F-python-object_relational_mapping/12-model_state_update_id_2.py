#!/usr/bin/python3
"""
    A script that updates a record using ORM
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and inserting a state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    search_query = session.query(State).filter_by(id=2).first()

    if search_query:
        search_query.name = "New Mexico"
        session.commit()
