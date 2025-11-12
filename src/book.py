class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity


    def update_info(self, title=None, author=None, genre=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
    
    
    def update_quantity(self, new_quantity):
        try:
            new_q = int(new_quantity)
            if new_q >= 0:
                self.quantity = new_q
            else:
                print("Quantity cannot be negative")
        except ValueError:
            print("Invalid quantity")
    
    
    def is_available(self):
        return self.quantity > 0
    
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Genre: {self.genre} - Available: {self.quantity}"