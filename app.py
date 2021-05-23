import flask
from flask import request, jsonify
from flask import abort
from flask import make_response
from flask import url_for

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
    return jsonify({'books': [make_public_book(book) for book in books]})

@app.route('/api/v1/resources/books/<int:id>', methods=['GET'])
def api_id(id):
    
    # Search for the given id
    result = [ book for book in books if book['id'] == id]

    if len(result) == 0 :
        abort (404)


    # jsonfy flask functino to convert the list of dictionaries
    return jsonify(result)


@app.route('/api/v1/resources/books', methods=['POST'])
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

@app.route('/api/v1/resources/books/<int:id>', methods =['PUT'])
def update_book(id):
    # seach on the global book var
    result = [book for book in books if book['id'] == id]

    # test if every parametes was recived
    if len(result) == 0:
        abort(404) # not found
    if not request.get_json():
        abort(400) # bad request
    if 'title'  in request.json and isinstance(type(request.json['title']),str):
        abort(400)
    if 'author'  in request.json and isinstance(type(request.json['title']),str):
        abort(400)
    if 'first_sentence'  in request.json and isinstance(type(request.json['first_sentence']),str):
        abort(400)
    if 'year_pushield'  in request.json and isinstance(type(request.json['year_pushield']),int):
        abort(400)

    # updant the values
    result[0]['title'] = request.json.get('title', result[0]['title'])
    result[0]['author'] = request.json.get('author', result[0]['author'])
    result[0]['first_sentence'] = request.json.get('first_sentence', result[0]['first_sentence'])
    result[0]['year_pushield'] = request.json.get('year_pushield', result[0]['year_pushield'])
    
    return jsonify({'book': result})

@app.route('/api/v1/resources/books/<int:id>', methods=['DELETE'])
def delete_book(id):

    # seach on the global book var
    result = [book for book in books if book['id']==id]

    # Verfiry existence
    if len(result) == 0:
        abort(404)

    # remove from books data storage
    result.remove(result[0])

    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    # add a custom mensage for not found book item
    return make_response(jsonify({'error':'Not found'}),404)

# expose de URL for user. Improviment on service interface
def make_public_book(book):
    new_book = {}

    for field in book:

        if field == 'id':
            new_book['uri'] = url_for('api_all', id=book['id'], _external=True)

        else:
            new_book[field] = book[field]
    
    return new_book




app.run()