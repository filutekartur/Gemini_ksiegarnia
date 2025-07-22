class Book():
    def __init__(self,title,author,year,availability=True):
        self.title=title
        self.author=author
        self.year=year
        self.availability=availability

    def desc(self):
        print(f"The {self.title} book, written by {self.author} in {self.year} is {"available" if self.availability else "unavailbable"}")