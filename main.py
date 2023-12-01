from tkinter import Button, Tk, Text, END

import customtkinter
from customtkinter import CTk

import addBook
import ui.loginGUI as loginGUI
import ui.dashboardGUI as dashboardGUI
import ui.accManageGUI as accManageGUI
import ui.addBookGUI as addBookGUI
import loginFunc
import editProf
import dashboardFunc
import ctypes
from datetime import datetime


root = CTk()
customtkinter.deactivate_automatic_dpi_awareness()
root.geometry("937x667")
root.configure(bg="red")
root.resizable(False, False)
current_frame = None

login_page = loginGUI.login_gui_start(root)
dashboard_page = dashboardGUI.dashboard_gui_start(root)
add_books_page = addBookGUI.add_book_gui_start(root)
acc_management_page = accManageGUI.acc_management_gui_start(root)

current_frame = login_page


username_entry = login_page.username_entry
password_entry = login_page.password_entry

book_list = None

widget_list = None

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


show_frame(login_page)
show_frame(dashboard_page)
show_frame(add_books_page)
show_frame(acc_management_page)
show_frame(login_page)


def configure_buttons():
    global widget_list

    for widget in widget_list:
        edit_button = widget.get_edit_button()
        delete_button = widget.get_delete_button()

        # Configure edit button command
        edit_button.configure(command=lambda isbn=widget.get_isbn(): on_button_click_add_books(isbn))
        delete_button.configure(command=lambda isbn=widget.get_isbn(): on_button_delete(isbn))


def on_button_delete(isbn):
    global widget_list

    dashboard_page.remove_book_list()
    print("Delete button clicked")
    dashboardFunc.delete_book(isbn)
    dashboardFunc.show_book_list(dashboard_page)
    widget_list = dashboardFunc.show_book_list(dashboard_page)
    configure_buttons()


def dashboard_reset():
    global book_list, widget_list
    dashboard_page.remove_book_list()
    widget_list = dashboardFunc.show_book_list(dashboard_page)
    book_list = dashboardFunc.book_list
    configure_buttons()
    show_frame(dashboard_page)


def on_button_click():
    global user_ID
    result, user_ID = loginFunc.verify_login(username_entry.get(), password_entry.get())
    print(result)
    get_uid()
    if result:
        print(dashboardFunc.get_first_name())
        dashboard_page.canvas.itemconfig(dashboard_page.name, text="Welcome back, " + dashboardFunc.get_first_name() + "!")
        dashboard_reset()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Incorrect email or password!", "Incorrect Credentials", 1)


def reset_entries():
    add_books_page.book_name_entry.delete("0.0", "end")
    add_books_page.author_entry.delete("0.0", "end")
    add_books_page.isbn_entry.delete("0.0", "end")
    add_books_page.price_entry.delete("0.0", "end")
    add_books_page.genre_entry.delete("0.0", "end")
    add_books_page.book_description_entry.delete("0.0", "end")
    add_books_page.stock_entry.delete("0.0", "end")


def on_button_click_add_books(isbn=None):
    print("Settings updated successfully")
    if isbn:
        reset_entries()
        book_info = dashboardFunc.retrieve_book(isbn)
        add_books_page.book_name_entry.insert("1.0", book_info.get('bookname', ''))
        add_books_page.author_entry.insert("1.0", book_info.get('author', ''))
        add_books_page.isbn_entry.insert("1.0", book_info.get('isbn', ''))
        add_books_page.price_entry.insert("1.0", book_info.get('amount', ''))
        add_books_page.genre_entry.insert("1.0", book_info.get('genre', ''))
        date_string = book_info.get('publication', '')
        add_books_page.date_published_entry.set_date(datetime.strptime(date_string, '%Y-%m-%d'))
        add_books_page.book_description_entry.insert("1.0", book_info.get('description', ''))
        add_books_page.stock_entry.insert("1.0", book_info.get('stock', ''))
        show_frame(add_books_page)
    else:
        reset_entries()
        show_frame(add_books_page)


def on_button_click_edit_settings():
    print(user_ID)
    if user_ID == user_ID:
        name_text = ""
        print("Settings updated successfully")
        acc_management_page.canvas.itemconfig(acc_management_page.name, text=dashboardFunc.get_last_name() + ",\n" + dashboardFunc.get_first_name())
        show_frame(acc_management_page)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def on_button_click_dashboard():
    dashboard_reset()


def on_button_click_edit_submit(): #Edit-Profile-Submit
    new_username = acc_management_page.new_username_entry.get("1.0", "end-1c")
    current_password = acc_management_page.current_password_entry.get("1.0", "end-1c")
    new_password = acc_management_page.new_password_entry.get("1.0", "end-1c")
    if current_password == password_entry.get() and (new_password != ''):
        try:
            editProf.edit_settings(new_username, new_password)
            print("Successful")
            ctypes.windll.user32.MessageBoxW(0, "Success!", "Logout now", 1)
            if new_password.get() == '':
                ctypes.windll.user32.MessageBoxW(0, "Invalid!", "Cannot leave the New Password Empty!", 1)


        except:
            ctypes.windll.user32.MessageBoxW(0, "Failed to update!", "Incorrect password!", 1)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def on_button_click_add_submit(): #Add-Book-Button
    bookname = add_books_page.book_name_entry.get("1.0", "end-1c")
    author = add_books_page.author_entry.get("1.0", "end-1c")
    isbn = add_books_page.isbn_entry.get("1.0", "end-1c")
    amount = add_books_page.price_entry.get("1.0", "end-1c")
    genre = add_books_page.genre_entry.get("1.0", "end-1c")
    publisher = str(add_books_page.date_published_entry.get_date())
    description = add_books_page.book_description_entry.get("1.0", "end-1c")
    stock = add_books_page.stock_entry.get("1.0", "end-1c")

    try:
        if not check_character_limit(amount, 10000):
            ctypes.windll.user32.MessageBoxW(0, "Book name is too long. Please enter a shorter name.", "Error", 1)
            return

        if not check_character_limit(amount, 1000000):
            ctypes.windll.user32.MessageBoxW(0, "Book name is too long. Please enter a shorter name.", "Error", 1)
            return

        amount = float(amount)
        stock = int(stock)
        print(amount)
        print(stock)

        if not check_character_limit(bookname, 44):
            ctypes.windll.user32.MessageBoxW(0, "Book name is too long. Please enter a shorter name.", "Error", 1)
            return

        if not check_character_limit(author, 22):
            ctypes.windll.user32.MessageBoxW(0, "Author name is too long. Please enter a shorter name.", "Error", 1)
            return

        if not addBook.is_valid_isbn(isbn):
            ctypes.windll.user32.MessageBoxW(0, "Invalid ISBN. Please enter a valid ISBN.", "Error", 1)
            return

        if bookname == '':
            ctypes.windll.user32.MessageBoxW(0, "Bookname cannot be empty. Please enter a valid bookname.", "Error", 1)
            return
        if author == '':
            ctypes.windll.user32.MessageBoxW(0, "Author cannot be empty. Please enter a valid author.", "Error", 1)
            return


    except:
        ctypes.windll.user32.MessageBoxW(0, "Invalid input. Please enter a valid value.", "Error", 1)
        return

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


def search_by_book_name(search_term):
    global book_list, widget_list
    result_dict = {}
    for key, value in book_list.items():
        if search_term.lower() in value['bookname'].lower():
            result_dict[key] = value

    dashboard_page.remove_book_list()
    widget_list = dashboardFunc.show_book_list(dashboard_page, True, result_dict)
    configure_buttons()


def check_character_limit(user_input, limit=44):
    return len(user_input) <= limit


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

search_entry.bind("<Return>", lambda x: search_by_book_name(search_entry.get()))

edit_submit_button.configure(command=lambda: on_button_click_edit_submit())
add_submit_button.configure(command=lambda: on_button_click_add_submit())

submit_button.configure(command=lambda: on_button_click())

root.mainloop()
