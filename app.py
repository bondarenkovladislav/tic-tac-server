"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
from pymongo import MongoClient
from flask import request

import json
from bson import ObjectId

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

app.config["MONGO_URI"] = "mongodb+srv://vlad123:qwerty123@tic-tac-toe-jtwsd.mongodb.net/scoreboard?retryWrites=true&w=majority"
# app.config['MONGO_DBNAME'] = 'scoreboard'
# app.config['SECRET_KEY'] = 'secret_key'


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return '<h1> Deployed </h1>'

# returns created instance
@app.route("/create-score", methods=["POST"])
def createScore():
    userName = request.args.get('userName')
    id = ObjectId()
    mongo.db.scoreboard.insert({"_id": id, "userName": userName, "winCount": 1})
    output = []
    for s in mongo.db.scoreboard.find({"_id": id}):
        output.append({'userName': s['userName'], 'winCount': s['winCount'], "_id": str(id)})
    return jsonify({'result': output})


@app.route('/set-score', methods=["PUT"])
def setScore():
    id = request.args.get("id")
    value = request.args.get('value')
    mongo.db.scoreboard.update({"_id": ObjectId(id)}, {"$set": {"winCount": int(value)}})
    return "done"

@app.route("/get-score")
def getScore():
    scores = mongo.db.scoreboard
    output = []
    for s in scores.find({}):
        output.append({'userName': s['userName'],'winCount': s['winCount'], "_id": str(s['_id'])})
    return jsonify({'result': output})



@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)
#
#
# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=600'
#     return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@socketio.on('message')
def handle_message(data):
    print('received message: ', data)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
    send('Recieved')

@socketio.on('connect')
def test_connect():
    send('Connected from server')


mongo = PyMongo(app)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

if __name__ == '__main__':
    socketio.run(app, cors_allowed_origins="*")
