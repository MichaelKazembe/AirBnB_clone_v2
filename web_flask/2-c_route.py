#!/usr/bin/python3
"""
    >A script that starts a Flask web application:
    >Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB!”
        /c/<text>: display “C followed by the value of text”
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


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ Function that displays 'C followed by the value of text' """
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
