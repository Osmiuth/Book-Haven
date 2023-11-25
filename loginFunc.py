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


def verify_login(username: str, password: str):
    try:
        auth.sign_in_with_email_and_password(username, password)
        user_info = auth.get_account_info(auth.current_user['idToken'])
        user_id = user_info['users'][0]['localId']
        return True, user_id
    except:
        return False, None
