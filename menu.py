import os
from library import Library
def menu(library):
    while True:
        print("Chose option: ")
        print("1. Show books: ")
        print("2. Add new book: ")
        print("3. Search book: ")
        print("4. Borrow/Return book: ")
        print("5. Exit: ")
        choice = int(input(""))
        if choice==1:
            library.get_books()
        if choice==2:
            library.new_book()
        if choice==3:
            library.search()
        if choice==4:
            library.borrow_return_book()
        if choice==5:
            break
        input("Press enter to continue....")
        os.system('cls')