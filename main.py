from tkinter import Button, Tk, Text
import ui.loginGUI as loginGUI
import ui.dashboardGUI as dashboardGUI
import ui.accManageGUI as accManageGUI
import ui.addBookGUI as addBookGUI
import loginFunc
import ctypes

root = Tk()
root.geometry("937x667")
root.configure(bg="red")
root.resizable(False, False)

current_frame = None

login_page = loginGUI.login_gui_start(root)
acc_management_page = accManageGUI.acc_management_gui_start(root)
dashboard_page = dashboardGUI.dashboard_gui_start(root)
add_book_page = addBookGUI.add_book_gui_start(root)

username_entry = login_page.username_entry
password_entry = login_page.password_entry

search_entry = dashboard_page.search_entry

submit_button = login_page.submit_button

book_list_canvas = dashboard_page.book_list_canvas

login_submit_button = login_page.submit_button


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


def on_button_click():
    result = False
    result = loginFunc.verify_login(username_entry.get(), password_entry.get())
    if result:
        print("works")
        show_frame(dashboard_page)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Incorrect email or password!", "Incorrect Credentials", 1)


submit_button.configure(command=lambda: on_button_click())

show_frame(login_page)
root.mainloop()
