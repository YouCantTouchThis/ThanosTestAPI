import flask
import json
from flask import request, jsonify
import random
from random import randint
app = flask.Flask(__name__)

quotes = [
	{"text": "Never give up, not till the fight is over!"},
	{"text": "You will survive!"},
	{"text": "Its our success during hardship that makes us strong"}
]

@app.route('/', methods=['GET'])
def home():
    return "wow"

@app.route('/api/v1/quotes', methods = ['GET'])
def api_all():
	x = randint(0, 2)
	return quotes[x]['text']


app.run()