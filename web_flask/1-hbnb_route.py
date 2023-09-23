#!/usr/bin/python3
"""
    >A script that starts a Flask web application:
    >Routes:
        /: display "Hello HBNB!"
        /hbnb: display "HBNB"
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Function that displays 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Function that displays 'HBNB' """
    return "HBNB!"


if __name__ == '__main__':
    app.run()
