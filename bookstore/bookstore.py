class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = [] #bc we need an empty list to store books in
    #needs get_books
    def get_books(self):
        return self.books
    #add_book
    def add_book(self, book):
        self.books.append(book)
    #needs search_books(author=,title=)
    def search_books(self, author=None, title=None):
        answer = []
        for book in self.books:
            if author in book.author or title in book.title:
                answer.append(book)
        return answer
        
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = [] #author also needs a list of books bc they can have multiple
    #needs add_book
    def add_book(self, book):
        self.books.append(book)
    #get_books
    def get_books(self):
        return self.books
        
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    #have to add the book to the author's list here
        self.author.add_book(self)