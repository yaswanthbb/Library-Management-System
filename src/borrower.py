class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []


    def update_contact(self, new_contact):
        self.contact = new_contact


    def borrow(self, isbn, due_date):
        self.borrowed_books.append((isbn, due_date))


    def return_book(self, isbn):
        for i, (b_isbn, _) in enumerate(self.borrowed_books):
            if b_isbn == isbn:
                self.borrowed_books.pop(i)
                return True
        return False


    def __str__(self):
        return f"{self.name} (ID: {self.membership_id}) - Contact: {self.contact}"