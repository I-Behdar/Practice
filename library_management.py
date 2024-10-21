import requests
import re

class Book:
    def __init__(self, title, author, publication_year, isbn, description):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.description = description
    
    # API Request: Use an open book-related API, like the Google Books API, to fetch book data based on user input (book title, author, or ISBN).
    
class Library(Book):
    def __init__(self):
        self.books = {}
    
    def add_books(self, book): # book info API - requests 
        if book.title not in self.books:
            self.books[book.title] = (book.author, book.publication_year, book.isbn, book.description)
            return f"{book.title} book was sucessfully added to th library."
        else:
            return f"{book.title} book already exists in the library."
    
    def book_dislpay(self):
        if not self.books:
            return "No books in library."
        else:
            return f"{self.books}"
    
    def search_books(self):
        book_search = input('search for a book by title/author/isbn: ').lower()
        
        pattern = re.compile(rf"{book_search}", re.IGNORECASE)
        found_books = []

        for title, details in self.books.items():
            if pattern.search(title) or any(pattern.search(detail) for detail in details):
                found_books.append(title)

        if not found_books:
            return "No result for your search!"
        else:
            return f"{"\n".join(found_books)} is in the library."  
    
book1 = Book("To Kill a Mockingbird", "Harper Lee", "1960", "9780061120084", 
             "A novel set in the 1930s that explores themes of racial injustice.")

book2 = Book("1984", "George Orwell", "1949", "9780451524935", 
             "A dystopian novel that presents a terrifying vision of")

library = Library()
print(library.add_books(book1))
print(library.add_books(book2))
print(library.book_dislpay())
print(library.search_books())

