from book import Book
class Library():
    def __init__(self,name):
        self.name = name
        self.books = []
    def get_books(self):
        print(f"\nBooks of {self.name}:\n")
        for book in self.books:
            book.desc()
    def set_book(self,book):
        self.books.append(book)
    def new_book(self):
        title = input("Podaj tytuł: ")
        author = input("Podaj autora: ")
        year = input("Podaj rok wydania książki: ")
        book = Book(title,author,year)
        self.set_book(book)
        print(f"Book {title} added to {self.name}")
    def search(self):
        query = input("Podaj tytuł książki który chcesz znaleźć")
        books = []
        for book in self.books:
            if query.lower() in book.title.lower():
                books.append(book)
        if books:
            print("Found :")
            for book in books:
                book.desc()
        else:
            print("Not found.")