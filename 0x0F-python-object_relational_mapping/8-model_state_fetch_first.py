#!/usr/bin/python3
"""
    A script that print only the first state in the database
    hbtn_0e_6_usa using ORM

"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and listing the state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_row = session.query(State).order_by(State.id).first()
    if first_row:
        print("{}: {}".format(first_row.id, first_row.name))
    else:
        print("Nothing")
    session.close()
