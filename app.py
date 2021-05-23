import flask
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

@app.route('/', methods=['GET'])
def home():
    return ''' 
    <h1> Distante Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>
    '''

@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():

    # checke if an ID was provided
    if 'id' in request.args:
        id = int(request.args['id'])

    else:
        return "error: no ID field provided. Check the request id field and provide it, please"
    
    # Creat the result list to send the result: list of dictionaies
    results = []

    # make a search on the global dictionary *book*
    for book in books:

        # add to results
        if book['id'] == id:
            results.append(book)

    # jsonfy flask functino to convert the list of dictionaries
    return jsonify(results)

app.run()