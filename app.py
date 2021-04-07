import Flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# fixed data to api interection
books = [
    {'id':0,
    'title':'A fire upon the Deep',
    'author':'Vernor Vinge',
    'first_sentence':'The coldsleep itself was dreamless',
    'year_pushield':'1992'},
    {'id':1,
    'title':'The Oner who walk away from omelas',
    'author':'Ursula K. le Guin',
    'first_sentence':'Whith a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
    'year_pushield':'1973'},
    {'id':2,
    'title':'Dhalgren',
    'author':'Samuel R. Delany',
    'first_sentence':'to wound the autumnal city',
    'year_pushield':'1975'}
]

