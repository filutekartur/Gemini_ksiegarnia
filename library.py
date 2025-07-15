class Library():
    def __init__(self):
        self.books = []
    def get_books(self):
        for book in self.books:
            book.desc()