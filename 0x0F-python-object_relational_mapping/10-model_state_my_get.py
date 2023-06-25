#!/usr/bin/python3
"""
 script that prints the State object with the
 name passed as argument from the database.
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

    # Query the State object from the database based on the provided name
    instance = session.query(State).filter(State.name == argv[4]).first()

    # Print the state's ID or a "Not found" message
    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))
