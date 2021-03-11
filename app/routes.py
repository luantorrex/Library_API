# External
import json
from flask import jsonify, make_response

# Internal
from app import app, books, db
from app.models import Book


@app.route('/', methods=['GET'])
def index():
    return make_response(jsonify({
        'msg': 'Library - Main Page'
    }))


@app.route('/client/<id_client>/books', methods=['GET'])
def list_loaned_books(id_client):
    loaned_books = books.list_loaned(id_client)

    return make_response(jsonify({
        'data': loaned_books
    }))


@app.route('/books/<id>/reserve', methods=['GET', 'POST'])
def book_reserve(id):   
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