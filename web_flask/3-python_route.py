#!/usr/bin/python3
"""
    >A script that starts a Flask web application:
    >Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the
            text variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the
            text variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
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
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ Function that displays 'C ', followed by the value of the text """
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is_cool"):
    """ Function that displays 'Python ', followed by the value of the text """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
