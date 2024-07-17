# this module is responsible for starting server

from app import app
from extension import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()