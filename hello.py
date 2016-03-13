#!flask/bin/python
from flask import Flask, jsonify
import http.client, urllib


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/assignment_tracker/api/v1.0/add', methods=['POST'])
def add():
    return

if __name__ == '__main__':
    app.run(debug=True)