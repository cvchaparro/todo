from flask import Flask

todo = Flask(__name__)

@todo.route('/')
def index():
    return '<a href="#">Sign Up</a><a href="#">Sign In</a>'
