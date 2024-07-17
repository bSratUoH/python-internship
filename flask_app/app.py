from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = ToDo.query.all()
    result = [{"id": todo.id, "title": todo.title, "description": todo.description, "completed": todo.completed} for todo in todos]
    return jsonify(result)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = ToDo(title=data['title'], description=data.get('description'))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"message": "ToDo item added successfully"}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
