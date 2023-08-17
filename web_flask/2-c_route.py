#!/usr/bin/python3
'''
A script that starts a Flask web application
'''

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
     '''Function that returns a simple string'''
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Second function. Prints on /hbnb'''
    return "HBNB"

@app.route("c/<text>", strict_slashes=False)
def c(text):
    '''Third function. Prints on /c/anything'''
    return f"C {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
