#!/usr/bin/python3
"""
    >A script that starts a Flask web application:
"""
from flask import Flask, render_template

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
    """ Function that displays 'C followed by value of text' """
    return f'C {text.replace("_", " ")}'


@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    """ Function that displays 'Python followed by text variable """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ Function that displays number n """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_html(n):
    """ Function that displays HMTL page """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
