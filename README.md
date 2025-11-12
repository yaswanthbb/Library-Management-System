# Library Management System (Python OOP - Fresher Level)

This is a Simple Library Managment System written in Python using basic Object-Oriented Programming (OOP) concepts.  
It allows Adding,Updating,Deleting books and borrowers, borrowing and returning books, and searching for availability of the books using title,author or genre and shows no of copies available

---

## Project Description

The system manages a small library where you can:
- Add, update, or remove books
- Add, update, or remove borrowers
- Borrow and return books
- Check due dates and overdue books
- Search books by title, author, or genre
- View how many copies are available

All data is stored lists, it resets every time you restart the program.  
---

## How to Run

### 1️⃣ Clone 
Clone this repo using 

```bash
git clone https://github.com/yaswanthbb/Library-Management-System.git
cd ./Library-Management-System
```

### 2️⃣ Run the Program
Make sure you have **Python 3.8+** installed.

Then open a terminal in the project folder and run:
```bash
python main.py
```

🧩 Object-Oriented Programming Concepts Used
--
Classes

* Book → Represents book details

* Borrower → Represents a person borrowing books

* Library → Manages all books and borrowers

Encapsulation

All data (like book lists, borrower lists) is stored inside the Library class

Methods

Each class defines actions (methods) that operate on its data — like add_book(), borrow_book(), etc.

Relationships

The Library class has many Book and Borrower objects.

Borrowing links a borrower to a book temporarily until it’s returned.