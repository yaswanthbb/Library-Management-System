from src.library import Library

def menu():
    print('\n--- |Welcome to Library Management System| ---')
    print('1. Add book')
    print('2. Update book')
    print('3. Remove book')
    print('4. Add borrower')
    print('5. Update borrower')
    print('6. Remove borrower')
    print('7. Borrow book')
    print('8. Return book')
    print('9. Search books')
    print('10. List all books')
    print('11. List all borrowers')
    print('12. Check overdue for borrower')
    print('0. Exit')


def main():
    library = Library()
    while True:
        menu()
        choice = input('Enter choice: ').strip()
        if choice == '0':
            print('Bye')
            break
        elif choice == '1':
            title = input('Title: ')
            author = input('Author: ')
            isbn = input('ISBN: ')
            genre = input('Genre: ')
            qty = input('Quantity: ')
            library.add_book(title, author, isbn, genre, qty)
        elif choice == '2':
            isbn = input('ISBN of book to update: ')
            title = input('New title (leave blank to skip): ')
            author = input('New author (leave blank to skip): ')
            genre = input('New genre (leave blank to skip): ')
            qty = input('New quantity (leave blank to skip): ')
            qty_val = None if qty.strip() == '' else qty
            library.update_book(isbn, title or None, author or None, genre or None, qty_val)
        elif choice == '3':
            isbn = input('ISBN to remove: ')
            library.remove_book(isbn)
        elif choice == '4':
            name = input('Name: ')
            contact = input('Contact: ')
            mid = input('Membership ID: ')
            library.add_borrower(name, contact, mid)
        elif choice == '5':
            mid = input('Membership ID: ')
            name = input('New name (leave blank to skip): ')
            contact = input('New contact (leave blank to skip): ')
            library.update_borrower(mid, name or None, contact or None)
        elif choice == '6':
            mid = input('Membership ID to remove: ')
            library.remove_borrower(mid)
        elif choice == '7':
            mid = input('Membership ID: ')
            isbn = input('ISBN to borrow: ')
            library.borrow_book(mid, isbn)
        elif choice == '8':
            mid = input('Membership ID: ')
            isbn = input('ISBN to return: ')
            library.return_book(mid, isbn)
        elif choice == '9':
            term = input('Search term: ')
            by = input('Search by (title/author/genre): ').strip().lower()
            if by not in ('title', 'author', 'genre'):
                by = 'title'
            results = library.search_books(term, by)
            if not results:
                print('No books found')
            else:
                for b in results:
                    print(b)
        elif choice == '10':
            for b in library.list_all_books():
                print(b)
        elif choice == '11':
            for br in library.list_all_borrowers():
                print(br)
        elif choice == '12':
            mid = input('Membership ID: ')
            overdue = library.check_overdue(mid)
            if not overdue:
                print('No overdue books')
            else:
                for isbn, due in overdue:
                    print(f'{isbn} due on {due.date()}')
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
