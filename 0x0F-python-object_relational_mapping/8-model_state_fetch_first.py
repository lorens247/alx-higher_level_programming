#!/usr/bin/python3
"""
A script that prints the first State object from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Construct the database URI using command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    # Create a database engine
    engine = create_engine(db_uri)

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the first State object from the database
    instance = session.query(State).order_by(State.id).first()

    # Print the state's details
    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
