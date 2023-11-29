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

ref = db.reference('Manager')
print(ref.get())

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def edit_settings(new_username, new_password):
    try:
        ref.child("username").set(new_username)
        ref.child("password").set(new_password)
        return True
    except:
        return False
