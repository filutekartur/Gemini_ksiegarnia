from book import Book
from library import Library
lib = Library()
a = Book("Mine","He",2000,True)
b= Book("Yours","Me",1999,False)
lib.set_book(a)
lib.set_book(b)
lib.get_books()