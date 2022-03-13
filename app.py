from flask import Flask

from controller.book_controller import get_books, get_book
from controller.hello_controller import hello_world, hello_again


def init_routing(flask_app: Flask):
    flask_app.add_url_rule("/", 'hello_world', hello_world, methods=['GET'])
    flask_app.add_url_rule("/again", 'hello_again', hello_again, methods=['POST'])
    flask_app.add_url_rule("/books", 'get_books', get_books, methods=['GET'])
    flask_app.add_url_rule("/book/<int:isbn>", 'get_book', get_book, methods=['GET'])


app = Flask(__name__)
init_routing(app)

if __name__ == '__main__':
    app.run()
