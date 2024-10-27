import requests
import re
import hashlib
import pwinput

class Book:
    def __init__(self, title, author, publication_year, isbn, description):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.description = description
    
class Library():
    def __init__(self):
        self.books = {}
        self.users = {}
    
    def fetch_api_add_books(self):  
        
        book_name = input("Enter the title of the book you would like to add to library: ")

        book_query = "+".join(book_name.lower().split())
        
        url = f"https://www.googleapis.com/books/v1/volumes?q={book_query}&key=AIzaSyCbJIvhkukzqGJkHwoRNAiXQalcfwLXvcw"

        response = requests.get(url)

        data = response.json()

        title = None
        authors = None
        isbn = None
        publication_year = None
        description = None

        for item in data['items']:
            try:
                volume_info = item.get('volumeInfo', {})
                title = volume_info.get('title', 'Unknown title')
                authors = volume_info.get('authors', ['Unknown author'])
                publication_year = volume_info.get('publishedDate', 'Unknown year')
                description = volume_info.get('description', 'no description found')

                industry_identifiers = volume_info.get('industryIdentifiers', [])
                if industry_identifiers:
                    for identifier in industry_identifiers:
                        if identifier['type'] == 'ISBN_13':
                            isbn = identifier.get('identifier', 'Unknown ISBN')
                            break
                        else:
                            isbn = identifier[0].get('identifier', 'Unknown ISBN')
                
                if book_name.lower() in title.lower():
                    break
            except Exception as e:
                print(f"Error processing the item {e}")
                continue

        book = Book(title=title, author=authors, publication_year=publication_year, isbn=isbn, description=description)

        if book.title not in self.books:
            self.books[book.title] = (book.author, book.publication_year, book.isbn, book.description)
            return f"{book.title} book was sucessfully added to the library."
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

class Member:
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.borrowed_books = {}

    def email_validation(self, email):
        email_spl = re.split(r"[.@]", email)

        if len(email_spl) < 3:
            raise ValueError("Invalid email!")

        first_part = re.match(r"^[a-zA-z0-9_.-]+$", email_spl[0])
        second_part = re.match(r"^[a-zA-z0-9_.-]+$", email_spl[1])
        third_part = email_spl[2]  
        
        if first_part and second_part and 2 <= len(third_part) <= 5 and third_part.isalpha():
            return email
        else:
            raise ValueError("Invalid email!")
    
    def password_validation(self, password):
        upper_check = any(i.isupper() for i in password)
        lower_check = any(i.islower() for i in password)
        num_check = any(i.isnumeric() for i in password)
        symbol_check = bool(re.search(r'[^a-zA-Z0-9]', password))
        if len(password) > 8 and upper_check and lower_check and num_check and symbol_check:
            return password
        else:
            raise ValueError("Invalid password!")   
    
    def sign_up(self):
        username = input("please enter your username: ").lower()
        while True:
            email = input("please enter your email: ").lower()
            password = pwinput.pwinput(prompt="please enter your password: ")

            try: 
                self.email_validation(email)
                self.password_validation(password)
                break
            except Exception as e:
                print(f"{e}, try again")

        if email not in library.users:
            password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.username = username
            self.email = email
            self.password = password_hash
            library.users[self.email] = (self.username, self.password)
            return f"{username} signed up sucessfully"
        else:
            return f"User already exists!"

    def log_in(self):
        while True:
            email = input("please enter your email: ").lower()
            password = pwinput.pwinput(prompt="please enter your password: ").lower()

            password_hash_login = hashlib.sha256(password.encode('utf-8')).hexdigest()
            
            if email in library.users and password_hash_login == library.users[email][1]:
                break
            else:
                print(f"Invalid credentials, try again!")
        
        return f"Welcome to your library {library.users[email][0]}." 
    
    def borrow_books(self):

        while True:
            borrowed_book_title = input("please enter the title of the book you would like to borrow: ").lower()

            if borrowed_book_title in library.books:
                if borrowed_book_title not in self.borrowed_books:
                    book_info = library.books[borrowed_book_title]
                    self.borrowed_books[borrowed_book_title] = book_info
                    return f"{borrowed_book_title} was added to your library."
                else:
                    print(f"You have already borrowed {borrowed_book_title}.")
                    continue
            else:
                print(f"Sorry, we don't have '{borrowed_book_title}' in library, try again!.")
                continue
    
    def return_books(self):
        return_book_title = input("please enter the title of the book you would like to return: ").lower()
        
        while True:
            if return_book_title in library.books:
                if return_book_title in self.borrowed_books:
                    del self.borrowed_books[return_book_title]
                    return f"{return_book_title} was returned and removed from your library."
                else:
                    print(f"{return_book_title} is not in your library.")
                    continue
            else:
                print(f"Sorry, we don't have '{return_book_title}' in library, try again!.")
                continue
    
class Subscription:
    def __init__(self, duration, amount):
        self.duration = duration
        self.amount = amount
        self.subscribed_users = {}

library = Library()
member = Member()
print(library.fetch_api_add_books())
# print(library.book_dislpay())
# print(library.search_books())
# print(member.sign_up())
# print(member.log_in())
print(member.borrow_books())
print(member.return_books())

