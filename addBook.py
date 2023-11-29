import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



firebaseConfig = {
    "apiKey": "AIzaSyDOdgrqn0uQMc_Mv6A1Sh6elSCmG6GwkKY",
    "authDomain": "book-haven-database.firebaseapp.com",
    "databaseURL": "https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "book-haven-database",
    "storageBucket": "book-haven-database.appspot.com",
    "messagingSenderId": "933105010594",
    "appId": "1:933105010594:web:82469970841c835bf054fb",
    "measurementId": "G-YFZQKZZDY5"
}
cred = credentials.Certificate('C:/book_haven/book-haven-database-firebase-adminsdk-1kg85-59592dcad6 (1).json')


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app'
})

ref = db.reference('BookManagement')
print(ref.get())

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def add_book(new_bookname, new_author, new_isbn, new_amount, new_bookID, new_genre, new_publisher, new_description, new_stock):
    try:
        ref.child("bookname").set(new_bookname)
        ref.child("author").set(new_author)
        ref.child("isbn").set(new_isbn)
        ref.child("amount").set(new_amount)
        ref.child("bookID").set(new_bookID)
        ref.child("genre").set(new_genre)
        ref.child("publisher").set(new_publisher)
        ref.child("description").set(new_description)
        ref.child("stock").set(new_stock)
        return True
    except:
        return False