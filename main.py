from tkinter import Button, Tk, Text

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
acc_management_page = accManageGUI.acc_management_gui_start(root)
add_books_page = addBookGUI.add_book_gui_start(root)

current_frame = login_page

username_entry = login_page.username_entry
password_entry = login_page.password_entry

search_entry = dashboard_page.search_entry

submit_button = login_page.submit_button

db_button1 = dashboard_page.dashboard_button
edit_settings_button1 = dashboard_page.edit_user_profile_button
add_books_button1 = dashboard_page.add_books_button

db_button2 = add_books_page.dashboard_button
edit_settings_button2 = add_books_page.edit_user_profile_button
add_books_button2 = add_books_page.add_books_button

db_button3 = acc_management_page.dashboard_button
edit_settings_button3 = acc_management_page.edit_user_profile_button
add_books_button3 = acc_management_page.add_books_button

book_list_canvas = dashboard_page.book_list_canvas

login_submit_button = login_page.submit_button

user_ID = None


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


def on_button_click():
    global user_ID
    result = loginFunc.verify_login(username_entry.get(), password_entry.get())
    print(result)
    if result:
        user_ID = loginFunc.verify_login(username_entry.get(), password_entry.get())
        print("works")
        print(user_ID)
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
        print("Settings updated successfully")
        show_frame(acc_management_page)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Unauthorized Access!", "There is a UID mismatch", 1)


def on_button_click_dashboard():
    show_frame(dashboard_page)


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

root.mainloop()
