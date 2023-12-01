import pyrebase
import firebase_admin
import ui.dashboardGUI as dashboardGUI
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth


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
cred = credentials.Certificate('book-haven-database-firebase-adminsdk-1kg85-59592dcad6 (1).json')


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://book-haven-database-default-rtdb.asia-southeast1.firebasedatabase.app'
}, name="2")

ref = db.reference('Manager')

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def edit_settings(new_username, new_password):
    try:
        if new_username == '':
            ref.child("password").set(new_password)
            auth.update_user("uyITqqTxJpNjRWxv5e5A0of2Hm23", password=new_password)
        else:
            ref.child("username").set(new_username)
            ref.child("password").set(new_password)
            auth.update_user("uyITqqTxJpNjRWxv5e5A0of2Hm23", display_name=new_username, password=new_password)
        return True
    except:
        return False