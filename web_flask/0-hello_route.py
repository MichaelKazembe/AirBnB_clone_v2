#!/usr/bin/python3
"""
    > A script that starts a Flask web application:
    > Routes:
        /: display “Hello HBNB!”
"""
from flask import Flask


app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_route():
    """ Function that displays 'Hello HBNB' """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
