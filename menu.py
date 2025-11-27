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
        while True:
            try:
                choice = int(input(""))
                if choice <1 or choice >5:
                    raise ValueError
            except ValueError:
                print("Pick correct number")
            else:
                break
        if choice==1:
            library.get_books()
        elif choice==2:
            library.new_book()
        elif choice==3:
            library.search()
        elif choice==4:
            library.borrow_return_book()
        elif choice==5:
            break
        input("Press enter to continue....")
        os.system('cls')