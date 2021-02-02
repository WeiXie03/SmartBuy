from flask import Flask, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'
