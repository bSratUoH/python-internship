# database layer
#  we will create a model for our todo list, which will be a table in our database.
from extension import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Boolean)
    

