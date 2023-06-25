#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database 
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

    # Query and print the State objects from the database that contain the letter 'a'
    for instance in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))
