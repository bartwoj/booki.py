class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def serialize(self):
        return {
            'title': self.title,
            'author': self.author,
            "isbn": self.isbn
        }
