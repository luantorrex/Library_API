# External
import json
from flask import jsonify, make_response, abort

# Internal
from app import app, books, db
from app.models import Book


@app.route('/', methods=['GET'])
def index():
    return make_response(jsonify({
        'msg': 'Library - Main Page'
    }))


@app.route('/client/<int:id_client>/books', methods=['GET'])
def list_loaned_books(id_client):
    if id_client is None or type(id_client) != int or not books.book_exists(id_client):
        abort(404, description="Resource not found")

    loaned_books = books.list_loaned(id_client)

    return make_response(jsonify({
        'data': loaned_books
    }))


@app.route('/books/<int:id>/reserve', methods=['GET', 'POST'])
def book_reserve(id):   
    if id is None or type(id) != int or not books.book_exists(id):
        abort(404, description="Resource not found")
    
    book_name = books.reserve(id)

    return make_response(jsonify({
        'msg': 'Book {} has been loaned.'.format(book_name)
    }))


@app.route('/books', methods=['GET'])
def list_all_books():   
    books_dict = books.list_all()
    
    return make_response(jsonify({
        'data': books_dict
    }))


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404