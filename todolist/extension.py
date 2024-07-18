# this file contains the initialization of the ORM object
# which is used to interact with the database
# the ORM object is created using the SQLAlchemy library

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
