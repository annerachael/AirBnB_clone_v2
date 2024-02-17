#!/usr/bin/python3
"""
script that displays Hello HBNB!
/hbnb: display HBNB
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display hello hbnb
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb_school():
    """
    Display hbnb
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
