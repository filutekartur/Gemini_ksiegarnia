from book import Book
import json
class Library():
    def __init__(self,name,file):
        self.name = name
        self.books = {}
        self.file = file
    def get_books(self):
        print(f"\nBooks of {self.name}:\n")
        for id,book in self.books.items():
            print(f"{id}. {book.desc()}")
    def set_book(self,book):
        self.books[str(len(self.books)+1)]=book
    def new_book(self):
        while True:
            title = input("Enter title: ")
            author = input("Enter author: ")
            if title and author:
                break
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
        for id,book in self.books.items():
            if query.lower() in book.title.lower():
                books.append(id)
        if books:
            print("Found:")
            for id in books:
                print(f"{id}. {self.books[id].desc()}")
        else:
            print("Not found.")
        return books
    def search(self):
        books=[]
        while True:
            #take a list of action from input
            option = [x for x in input("Choose search options?\n"
                                        "T - Title\n"
                                        "A - Author\n"
                                        "Y - Release year\n")]
            #check if any element is diferent than accepted, produce True/Fale list and react if there is not False inside
            if False not in[x in ["A","T","Y"] for x in option] and option:
                break
        for x in option:
            books=self.find(books,x)

        query = input("Enter title which you want to find: ")
        books = []
        for id,book in self.books.items():
            if query.lower() in book.title.lower():
                books.append(id)
        if books:
            print("Found:")
            for id in books:
                print(f"{id}. {self.books[id].desc()}")
        else:
            print("Not found.")
        return books
    
    def find(self,books,option):
        books = books if books else self.books # to jest lista a drugie dictionary 
        query = input(f"Enter {self.TAY(option)} you want to find: ")
        for id,book in self.books.items():# tutaj musze szukać po lokalnym books a nie po self
                if query.lower() in (book.title.lower() if option =="T" else book.author.lower() if option=="A" else book.author.year()):
                    books.append(id)
        if option == "T":
            for id,book in self.books.items():
                if query.lower() in book.title.lower():
                    books.append(id)
        if option == "A":
            for id,book in self.books.items():
                if query.lower() in book.title.lower():
                    books.append(id)
        if option == "Y":
            for id,book in self.books.items():
                if query.lower() in book.title.lower():
                    books.append(id)
    def TAY(option):
        if option=="T":
            return "Title"
        if option=="A":
            return "Author"
        if option=="Y":
            return "Year"
        else:
            return ""
    
    def borrow_book(self,book):
        if self.books[book].availability:
            self.books[book].availability = False
            print(f"{self.books[book].title}, borrowed.")
        else:
            print(f"{self.books[book].title}, is already borrowed")
    def return_book(self,book):
        if not self.books[book].availability:
            self.books[book].availability = True
            print(f"{self.books[book].title}, returned.")
        else:
            print(f"{self.books[book].title}, is already returned")
    def borrow_return_book(self):
        books = self.search()
        if books:
            while True:
                try:
                    choice = int(input("Which book do you mean, pick number? "))
                    if choice <1 or choice > len(books):
                        raise ValueError
                except ValueError:
                    print("Pick correct number!")
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
    def read_file(self):
        with open(self.file, encoding="utf-8") as f:
            self.books={
                k : Book(*l) 
                for k,l in json.loads(f.read()).items()
            }
            #tworzy dict z odczytanego pliku, * rozszywa liste na pojedyncze argumenty
    def write_file(self):
        with open(self.file, "w",encoding="utf-8") as f:
            data={ id : [book.title,book.author,book.year,book.availability] for id,book in self.books.items()}
            f.write(json.dumps(data,indent=4,ensure_ascii=False))

            # {"1": ["Tajemnice Starego Lasu", "Anna Kowalska", 2018, true],
            # "1": ["Tajemnice Starego Lasu", "Anna Kowalska", 2018, true]}