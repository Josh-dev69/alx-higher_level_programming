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
    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, pwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    fetch_first = session.query(State).order_by(State.id).first()
    if fetch_first:
        print("{}: {}".format(fetch_first.id, fetch_first.name))
    else:
        print("Nothing")
    session.close()
