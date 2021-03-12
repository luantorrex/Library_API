from app import db
from app.models import Book
from datetime import datetime

def list_all():
    books_db = Book.query.all()
    books_dict = {}

    for book in books_db:
        books_dict[book.id] = {}
        
        for k, v in book.__dict__.items():            
            if k == '_sa_instance_state':
                continue
            elif k == 'loaned':
                v = 'Emprestado' if book.loaned else 'Disponivel'
            else:
                books_dict[book.id][k] = v
    
    return books_dict


def list_loaned(id_client):
    loaned_books_db = Book.query.filter_by(
        loaned=True,
        id=id_client
    )
    loaned_books_dict = {}

    for book in loaned_books_db:
        if book.date_loaned:
            days_late = (datetime.today() - book.date_loaned).days
            if days_late == 0:
                late_fee = 0
            elif days_late <= 3:
                late_fee = 0.2
            elif days_late > 3:
                late_fee = 0.4
            elif days_late > 5:
                late_fee = 0.6
        else:
            late_fee = None

        loaned_books_dict[book.id] = {
            'name': book.name,
            'late_fee': late_fee
        }
    
    return loaned_books_dict


def reserve(id_):
    book = Book.query.filter_by(id=id_).first()
    book.loaned = True
    book.date_loaned = datetime.today()

    db.session.add(book)
    db.session.commit()

    return book.name


def book_exists(id_):
    book = Book.query.filter_by(id=id_).first()
    if book:
        return True
    else:
        return False