import flask
from flask import request, jsonify
from flask import abort
from flask import make_response

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

@app.route('/', methods=['GET'])
def home():
    return ''' 
    <h1> Distante Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>
    '''

@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books/<int:id>', methods=['GET'])
def api_id(id):
    
    # Search for the given id
    result = [ book for book in books if book['id'] == id]

    if len(result) == 0 :
        abort (404)


    # jsonfy flask functino to convert the list of dictionaries
    return jsonify(result)


@app.route('/api/v1/resources/books/', methods=['POST'])
def creacte_book():

    if not request.json or not 'title' in request.json:
        #bad request
        abort (400)

    # all data was provided, so add a new book
    book = {
        'id': books[-1]['id']+1,
    'title': request.json['title'],
    'author':request.json['author'],
    'first_sentence':request.json['first_sentence'],
    'year_pushield':request.json['year_pushield']}

    # append to global books var
    books.append(book)

    return jsonify({'book':book}),201


@app.errorhandler(404)
def not_found(error):
    # add a custom mensage for not found book item
    return make_response(jsonify({'error':'Not found'}),404)



app.run()