from flask import jsonify

from model.Book import Book


def get_books():
    return jsonify([e.serialize() for e in [Book('Clean Code', 'Robert C. Martin', '9780132350884')]])


def get_book(isbn: int):
    return jsonify(Book('Clean Code', 'Robert C. Martin', '9780132350884').serialize())



