#!/usr/bin/python3
'''A script that starts a Flask web application'''


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    '''It close the session'''
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    '''Shows the states in an HTML page'''
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    '''Shows the cities of a state in a HTML page'''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)