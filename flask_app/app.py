from flask import Flask


app = Flask(__name__)

# print(dir(app))

# routes
# URLS

@app.route('/', methods=['POST'])
def hello():
    return "Hello World!"

@app.route('/hello/<name>')
def gretting(name):
    return f"Hello {name}!"



app.run()

