import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('book-haven-database-firebase-adminsdk-1kg85-59592dcad6 (1).json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app'
})

ref = db.reference('BookManagement')

def add_book(new_bookname, new_author, new_isbn, new_amount, new_genre, new_publisher, new_description, new_stock):
    try:
        ref.child(new_isbn).child("bookname").set(new_bookname)
        ref.child(new_isbn).child("author").set(new_author)
        ref.child(new_isbn).child("isbn").set(new_isbn)
        ref.child(new_isbn).child("amount").set(new_amount)
        ref.child(new_isbn).child("genre").set(new_genre)
        ref.child(new_isbn).child("publisher").set(new_publisher)
        ref.child(new_isbn).child("description").set(new_description)
        ref.child(new_isbn).child("stock").set(new_stock)
        return True
    except:
        return False