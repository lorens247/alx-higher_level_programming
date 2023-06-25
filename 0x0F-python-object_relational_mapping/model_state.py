#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class represents a state in the application."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)  # Primary key column for the state
    name = Column(String(128), nullable=False)  # Name column for the state, must be provided
