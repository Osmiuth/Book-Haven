from tkinter import Button, Tk, Text

import addBook
import retrieveBooks
import ui.loginGUI as loginGUI
import ui.dashboardGUI as dashboardGUI
import ui.accManageGUI as accManageGUI
import ui.addBookGUI as addBookGUI
import loginFunc
import editProf
import ctypes

root = Tk()
root.geometry("937x667")
root.configure(bg="red")
root.resizable(False, False)

login_page = loginGUI.login_gui_start(root)
dashboard_page = dashboardGUI.dashboard_gui_start(root)
add_books_page = addBookGUI.add_book_gui_start(root)
acc_management_page = accManageGUI.acc_management_gui_start(root)


current_frame = login_page

username_entry = login_page.username_entry
password_entry = login_page.password_entry

search_entry = dashboard_page.search_entry

submit_button = login_page.submit_button

edit_submit_button = acc_management_page.submit_button
add_submit_button = add_books_page.submit_button

db_button1 = dashboard_page.dashboard_button
edit_settings_button1 = dashboard_page.edit_user_profile_button
add_books_button1 = dashboard_page.add_books_button

db_button2 = add_books_page.dashboard_button
edit_settings_button2 = add_books_page.edit_user_profile_button
add_books_button2 = add_books_page.add_books_button

db_button3 = acc_management_page.dashboard_button
edit_settings_button3 = acc_management_page.edit_user_profile_button
add_books_button3 = acc_management_page.add_books_button
name_text = acc_management_page.name

book_list_canvas = dashboard_page.book_list_canvas

login_submit_button = login_page.submit_button

book_list_frame = dashboard_page.book_list_frame

user_ID = None


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


def on_button_click():
    global user_ID
    result, user_ID = loginFunc.verify_login(username_entry.get(), password_entry.get())
    print(result)
    get_uid()
    if result:
        show_frame(dashboard_page)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Incorrect email or password!", "Incorrect Credentials", 1)


def on_button_click_add_books():
    if user_ID == user_ID:
        print("Settings updated successfully")
        show_frame(add_books_page)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def on_button_click_edit_settings():
    print(user_ID)
    if user_ID == user_ID:
        name_text = ""
        print("Settings updated successfully")
        show_frame(acc_management_page)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def on_button_click_dashboard():
    show_frame(dashboard_page)


def on_button_click_edit_submit(): #Edit-Profile-Submit
    new_username = acc_management_page.new_username_entry.get("1.0", "end-1c")
    current_password = acc_management_page.current_password_entry.get("1.0", "end-1c")
    new_password = acc_management_page.new_password_entry.get("1.0", "end-1c")
    if current_password == password_entry.get() and (new_password != ''):
        try:
            editProf.edit_settings(new_username, new_password)
            print("Successful")
            ctypes.windll.user32.MessageBoxW(0, "Success!", "Logout now", 1)
        except:
            print("Failed")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def on_button_click_add_submit(): #Add-Book-Button
    bookname = add_books_page.book_name_entry.get("1.0", "end-1c")
    author = add_books_page.author_entry.get("1.0", "end-1c")
    isbn = add_books_page.isbn_entry.get("1.0", "end-1c")
    amount = add_books_page.price_entry.get("1.0", "end-1c")
    genre = add_books_page.genre_entry.get("1.0", "end-1c")
    publisher = add_books_page.date_published_entry.get("1.0", "end-1c")
    description = add_books_page.book_description_entry.get("1.0", "end-1c")
    stock = add_books_page.stock_entry.get("1.0", "end-1c")

    try:
        amount = float(amount)
        stock = int(stock)
        print(amount)
        print(stock)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Invalid input. Please enter a valid value.", "Error", 1)

    if password_entry.get() == password_entry.get():
        try:
            addBook.add_book(bookname, author, isbn, amount, genre, publisher, description, stock)
        except:
            print("Failed")
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def get_uid():
    print(user_ID, "user_ID <---")
    return user_ID


submit_button.configure(command=lambda: on_button_click())

db_button1.configure(command=lambda: on_button_click_dashboard())
add_books_button1.configure(command=lambda: on_button_click_add_books())
edit_settings_button1.configure(command=lambda: on_button_click_edit_settings())

db_button2.configure(command=lambda: on_button_click_dashboard())
add_books_button2.configure(command=lambda: on_button_click_add_books())
edit_settings_button2.configure(command=lambda: on_button_click_edit_settings())

db_button3.configure(command=lambda: on_button_click_dashboard())
add_books_button3.configure(command=lambda: on_button_click_add_books())
edit_settings_button3.configure(command=lambda: on_button_click_edit_settings())

edit_submit_button.configure(command=lambda: on_button_click_edit_submit())
add_submit_button.configure(command=lambda: on_button_click_add_submit())

submit_button.configure(command=lambda: on_button_click())


root.mainloop()
