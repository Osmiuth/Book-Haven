import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Use a unique app name when initializing
cred = credentials.Certificate('book-haven-database-firebase-adminsdk-1kg85-59592dcad6 (1).json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app'}, name='3')

# Use the correct app name when accessing the reference
ref = db.reference('BookManagement')

book_list = None


def retrieve_book(isbn):
    book = ref.child(isbn).get()
    return book


def show_book_list(dashboard_page, is_searching=False, list_of_books=None):
    global book_list
    books_data = None
    book_widgets = []

    if not is_searching:
        books_data = ref.get()
        print(books_data)
        book_list = books_data
    else:
        print("Going into Searching mode...")
        books_data = list_of_books

    if books_data:
        row = 0
        col = 0

        for isbn, book_info in books_data.items():
            isbnnum = book_info.get('isbn', '')
            book_title = book_info.get('bookname', '')
            author = book_info.get('author', '')
            date_added = book_info.get('publisher', '')
            stock = book_info.get('stock', '')
            price = book_info.get('amount', '')

            # Create a book widget using the provided function
            book_widget = dashboard_page.show_book(isbnnum, book_title, author, date_added, stock, price, row, col)

            # Append the created widget to the list
            book_widgets.append(book_widget)

            # Update column and row based on the rule (move to the next row if two columns are filled)
            col += 1
            if col == 2:
                col = 0
                row += 1

    return book_widgets

