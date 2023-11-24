#!/usr/bin/python3
"""
    A a script that prints the State object with the name passed as 
    argument from the database hbtn_0e_6_usa using ORM
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
    
    requested_state = session.query(State).filter(State.name == argv[4]).first()

    if requested_state:
        print("{}".format(requested_state.id))
    else:
        print("Not found")

    session.close()
