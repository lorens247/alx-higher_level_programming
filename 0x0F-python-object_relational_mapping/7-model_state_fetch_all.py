#!/usr/bin/python3
"""
A script that lists all State objects from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access and get the states from the database.
    """

    # Construct the database URI using command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create a database engine
    engine = create_engine(db_uri)

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query and print the State objects from the database
    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
