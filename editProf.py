import pyrebase

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

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def edit_settings(user_id, new):
    try:
        auth.child("users").child(user_id).child("settings").update(new)
        return True
    except:
        return False
