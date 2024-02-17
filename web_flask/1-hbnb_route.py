#!/usr/bin/python3
"""
script that runs flask
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    function that returns url
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_school():
    """
    function that returns url
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
