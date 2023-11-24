#!/usr/bin/python3
"""
This class represent the City which work
with ORM objects

"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The city id of the class
        name (str): The city name of the class
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
