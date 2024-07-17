# routes and views for the flask application

from flask import Flask, request, jsonify
from models import Todo
from extension import db
from utils import get_data


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)


# CRUD - Create, Read, Update, Delete


@app.route('/tasks', methods=['POST'])
def create_task():
    # try:
    user_data = request.get_json()
    todo_obj = Todo(title=user_data['title'], status=user_data['status'])
    db.session.add(todo_obj)
    db.session.commit()
    return 'Task created successfully', 201
    # except Exception as e:
    #     return "unexpected error has occurred", 500


@app.route('/tasks', methods=['GET'])
def get_task():
    # try:
    todo_data = Todo.query.all()
    data = get_data(todo_data)
    return jsonify(data), 200
    # except Exception as e:
    #     return "unexpected error has occurred", 500

