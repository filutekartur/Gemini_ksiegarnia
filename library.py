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
        title = input("Enter title: ")
        author = input("Enter author: ")
        while True:
            try:
                year = int(input("Enter release year: "))
            except ValueError as ve:
                print(f"Enter correct year.")
            else:
                break
        book = Book(title,author,year)
        self.set_book(book)
        print(f"Book {title} added to {self.name}")
    def search(self):
        query = input("Enter title which you want to find: ")
        books = []
        for book in self.books:
            if query.lower() in book.title.lower():
                books.append(book)
        if books:
            print("Found :")
            i=1
            for book in books:
                print(f"{i}. ",end='')
                book.desc()
                i+=1
        else:
            print("Not found.")
        return books
    def borrow_book(self,book):
        if book.availability:
            book.availability = False
            print(f"{book.title}, borrowed.")
        else:
            print(f"{book.title}, is already borrowed")
    def return_book(self,book):
        if not book.availability:
            book.availability = True
            print(f"{book.title}, returned.")
        else:
            print(f"{book.title}, is already returned")
    def borrow_return_book(self):
        books = self.search()
        if books:
            choice = 0
            while choice > len(books) or choice < 1:
                while True:
                    try:
                        choice = int(input("Which book do you mean, pick number? "))
                    except ValueError:
                        print("Pick number!")
                    else:
                        break
            while True:
                action = input("what do you want to do?\nB = Borrow\nR = Return\n")
                if action == "B":
                    self.borrow_book(books[choice-1])
                    break
                elif action == "R":
                    self.return_book(books[choice-1])
                    break
                else:
                    print("Wrong action!")
                    continue