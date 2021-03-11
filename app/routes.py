# External
import json
from flask import jsonify, make_response

# Internal
from app import app, books, db
from app.models import Book


@app.route('/')
def index():
    return make_response(jsonify({
        'msg': 'Library - Main Page'
    }))


@app.route('/books')
def list_all_books():   
    books_dict = books.list_all()
    
    return make_response(jsonify({
        'data': books_dict
    }))


@app.route('/client/<id_client>/books')
def list_loaned_books(id_client):
    loaned_books = books.list_loaned()

    return make_response(jsonify({
        
    }))


""" @app.route('/books/<id>/reserva')
def list_all_books():   
    books_dict = books.list_all()
    
    return make_response(jsonify({
        'data': books_dict
    })) """

""" 
    TO-DO: 
        
    EMPRESTIMO:
        - LIVROS EMPRESTADOS POR CLIENTE
        - LISTAGEM DE LIVROS EMPRESTADOS
        - LIVROS COM ATRASO PAGAM MULTA
    
    RESERVA:
        - RESERVAR LIVRO POR ID
"""