import ctypes

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('book-haven-database-firebase-adminsdk-1kg85-59592dcad6 (1).json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app'
})

ref = db.reference('BookManagement')
print(ref.get())

def add_book(new_bookname, new_author, new_isbn, new_amount, new_genre, new_publisher, new_description, new_stock):
    try:
        x = is_valid_isbn(new_isbn)
        if x == True:
            if ref.child(new_isbn):
                y = ctypes.windll.user32.MessageBoxW(0, "Would you like to proceed?", "ISBN duplicate detected!", 1)
                if y == 1:
                    ref.child(new_isbn).child("bookname").set(new_bookname)
                    ref.child(new_isbn).child("author").set(new_author)
                    ref.child(new_isbn).child("isbn").set(new_isbn)
                    ref.child(new_isbn).child("amount").set(new_amount)
                    ref.child(new_isbn).child("genre").set(new_genre)
                    ref.child(new_isbn).child("publisher").set(new_publisher)
                    ref.child(new_isbn).child("description").set(new_description)
                    ref.child(new_isbn).child("stock").set(new_stock)
                    ctypes.windll.user32.MessageBoxW(0, "Successful!", "Success!", 1)
                else:
                    return print('ISBN exists')
        else:
            ref.child(new_isbn).child("bookname").set(new_bookname)
            ref.child(new_isbn).child("author").set(new_author)
            ref.child(new_isbn).child("isbn").set(new_isbn)
            ref.child(new_isbn).child("amount").set(new_amount)
            ref.child(new_isbn).child("genre").set(new_genre)
            ref.child(new_isbn).child("publisher").set(new_publisher)
            ref.child(new_isbn).child("description").set(new_description)
            ref.child(new_isbn).child("stock").set(new_stock)
            ctypes.windll.user32.MessageBoxW(0, "Successful!", "Success!", 1)
        return True
    except:
        return False


def is_valid_isbn(isbn):
    # Remove any dashes or spaces from the input
    isbn = isbn.replace('-', '').replace(' ', '')

    # Check if the length is either 10 or 13
    if len(isbn) not in [10, 13]:
        return False

    # Check if the first digits are numeric
    if not isbn[:-1].isdigit():
        return False

    # Check the last digit
    if len(isbn) == 10:
        if not (isbn[-1].isdigit() or isbn[-1].upper() == 'X'):
            return False
        # Calculate and check the ISBN-10 checksum
        checksum = sum(int(digit) * (10 - index) for index, digit in enumerate(isbn[:-1]))
        checksum = (11 - (checksum % 11)) % 11
        if isbn[-1].upper() == 'X':
            return checksum == 10
        else:
            return checksum == int(isbn[-1])
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
        # Calculate and check the ISBN-13 checksum
        checksum = sum(int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(isbn[:-1]))
        checksum = (10 - (checksum % 10)) % 10
        return checksum == int(isbn[-1])
