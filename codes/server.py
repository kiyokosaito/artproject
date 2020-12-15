from flask import Flask, url_for, request, redirect, abort, jsonify
from ArtDao import artDao
#これが提出用のサーバー

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

#getAll
# curl http://127.0.0.1:5000/art
@app.route('/art')
def getAll():
    return jsonify(artDao.getAll())

#findById
@app.route('/art/<int:id>')
def findById(id):
    return jsonify(artDao.findById(id))


@app.route('/art', methods = ['POST'])
def create():

    if not request.json:
        abort (400)

    art = {
        'id': request.json['id'],
        'title': request.json['title'],
        'author': request.json['author'],
        'price': request.json['price']

    }
    
    return jsonify(artDao.create(art))

#update
# curl -X PUT -d "{\"title\":\"blue sky\", \"price\":5555}" -H Content-Type:application/json http://127.0.0.1:5000/art/1
@app.route('/art/<int:id>', methods = ['PUT'])
def update(id):
    foundart = artDao.findById(id)
    print(foundart)
    if foundart == {} :
        return jsonify({}), 404
    currentArt = foundart
    if 'title' in request.json:
        currentArt['title'] =request.json['title']
    if 'author' in request.json:
        currentArt['author'] =request.json['author']
    if 'price' in request.json:
        currentArt['price'] =request.json['price']
    artDao.update(currentArt)


    return jsonify(currentArt) 

#delete
# curl -X DELETE http://127.0.0.1:5000/art/3
@app.route('/art/<int:id>', methods = ['DELETE'])
def delete(id):
    artDao.delete(id)
    return jsonify({'done':True})

if __name__ == "__main__":
    app.run(debug=True)