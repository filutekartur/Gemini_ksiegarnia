from book import Book
from library import Library
from menu import menu
lib = Library("Library","books.json")
# a = Book("Miney","He",2000,True)
# # b= Book("Yoursy","Me",1999,False)
# lib.set_book(a)
# lib.set_book(b)
#lib.get_books()
lib.read_file()
menu(lib)
lib.write_file()