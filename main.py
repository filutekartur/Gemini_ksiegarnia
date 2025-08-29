from book import Book
from library import Library
from menu import menu
lib = Library("Biblioteka")
a = Book("Miney","He",2000,True)
b= Book("Yoursy","Me",1999,False)
lib.set_book(a)
lib.set_book(b)
#lib.get_books()
#lib.borrow_return_book()
menu(lib)