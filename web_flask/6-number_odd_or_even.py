#!/usr/bin/python3
'''Flask WSGI for multiple routes'''


from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''First function. Prints on /'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_hbnb():
    '''Second function. Prints on /hbnb'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    '''Third function. Prints on /c/anything'''
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text='is cool'):
    '''Fourth function. Prints on /python/anything'''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def only_int(n):
    '''Fifth function. Prints on number if n is int'''
    return "{} is a number".format(n)


@app.route("/number_template/<n>")
def n_temp(n):
    '''Route for /number_template/<n>'''
    return render_template('5-number.html', title='HBNB', n=n)


@app.route("/number_odd_or_even/<n>")
def n_odd(n):
    '''Seventh function. Prints a HTML template'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")