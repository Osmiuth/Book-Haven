import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Use a unique app name when initializing
cred = credentials.Certificate('book-haven-database-firebase-adminsdk-1kg85-59592dcad6 (1).json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app'}, name='3')

# Use the correct app name when accessing the reference
ref = db.reference('BookManagement')

def retrieve_book(isbn):
    book = ref.child(isbn).get()
    return book

def retrieve_all_books():
    books = ref.get()
    return books