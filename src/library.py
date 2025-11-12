from datetime import datetime, timedelta
from src.book import Book
from src.borrower import Borrower

class Library:
    def __init__(self):
        self.books = [] 
        self.borrowers = [] 

    def add_book(self, title, author, isbn, genre, quantity):
        if self.find_book_by_isbn(isbn):
            print("Book with this ISBN already exists. Use update if needed.")
            return False
        try:
            q = int(quantity)
            if q < 0:
                print('Quantity cannot be negative')
                return False
        except ValueError:
            print('Invalid quantity')
            return False
        book = Book(title, author, isbn, genre, q)
        self.books.append(book)
        print(f"{title} by {author} Added Successfully")
        return True

    def update_book(self, isbn, title=None, author=None, genre=None, quantity=None):
        book = self.find_book_by_isbn(isbn)
        if not book:
            print('Book not found')
            return False
        old_title = book.title
        old_author = book.author
        book.update_info(title, author, genre)
        if quantity is not None:
            book.update_quantity(quantity)
        print('Book Updated Successfully')
        return True

    def remove_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            print("Book Removed Successfully")
            return True
        print('Book not found')
        return False

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_books(self, query, by='title'):
        results = []
        q = query.lower()
        for book in self.books:
            if by == 'title' and q in book.title.lower():
                results.append(book)
            elif by == 'author' and q in book.author.lower():
                results.append(book)
            elif by == 'genre' and q in book.genre.lower():
                results.append(book)
        return results

    def add_borrower(self, name, contact, membership_id):
        if self.find_borrower_by_id(membership_id):
            print('Borrower with this ID already exists')
            return False
        borrower = Borrower(name, contact, membership_id)
        self.borrowers.append(borrower)
        print("Borrower Added Successfully")
        return True

    def update_borrower(self, membership_id, name=None, contact=None):
        b = self.find_borrower_by_id(membership_id)
        if not b:
            print('Borrower not found')
            return False
        if name:
            b.name = name
        if contact:
            b.contact = contact
        print("Borrower Updated Successfully")
        return True

    def remove_borrower(self, membership_id):
        b = self.find_borrower_by_id(membership_id)
        if b:
            self.borrowers.remove(b)
            print("Borrower Removed Successfully")
            return True
        print('Borrower not found')
        return False

    def find_borrower_by_id(self, membership_id):
        for b in self.borrowers:
            if b.membership_id == membership_id:
                return b
        return None

    def borrow_book(self, membership_id, isbn, days=14):
        b = self.find_borrower_by_id(membership_id)
        if not b:
            print('Borrower not found')
            return False
        book = self.find_book_by_isbn(isbn)
        if not book:
            print('Book not found')
            return False
        if not book.is_available():
            print('Book not available')
            return False
        book.quantity -= 1
        due_date = datetime.now() + timedelta(days=days)
        b.borrow(isbn, due_date)
        print(f'Book borrowed. Due date: {due_date.date()}')
        return True

    def return_book(self, membership_id, isbn):
        b = self.find_borrower_by_id(membership_id)
        if not b:
            print('Borrower not found')
            return False
        book = self.find_book_by_isbn(isbn)
        if not book:
            print('Book not found in library records')
            return False
        ok = b.return_book(isbn)
        if not ok:
            print('This borrower did not borrow this book')
            return False
        book.quantity += 1
        print('Book returned successfully')
        return True

    def check_overdue(self, membership_id):
        b = self.find_borrower_by_id(membership_id)
        if not b:
            print('Borrower not found')
            return []
        overdue = []
        now = datetime.now()
        for isbn, due in b.borrowed_books:
            if now > due:
                overdue.append((isbn, due))
        return overdue

    def list_all_books(self):
        return self.books

    def list_all_borrowers(self):
        return self.borrowers
