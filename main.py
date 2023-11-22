from tkinter import Tk, Text, Button
import ui.loginGUI as loginGUI
import ui.dashboardGUI as dashboardGUI

root = Tk()
root.geometry("937x667")
root.configure(bg="red")
root.resizable(False, False)

current_frame = None

login_page = loginGUI.login_gui_start(root)
dashboard_page = dashboardGUI.dashboard_gui_start(root)

username_entry = login_page.username_entry
password_entry = login_page.password_entry

search_entry = dashboard_page.search_entry

book_list_canvas = dashboard_page.book_list_canvas

login_submit_button = login_page.submit_button


def show_frame(frame_to_show):
    global current_frame
    if current_frame:
        current_frame.pack_forget()

    current_frame = frame_to_show
    frame_to_show.pack(fill="both", expand=True)


def error_message(msg):
    """
    error_message creates a popup window with the error message msg
    :param msg: the message to be displayed
    :return: None
    """
    popup = Tk()
    popup.wm_title("Error!")
    popup.geometry("300x100")
    popup.configure(bg="#925FE2")
    label = Text(popup, text=msg, bg="#925FE2", fg="white", font=("Poppins Medium", 16 * -1))
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#1C1D21", fg="white", font=("Poppins Medium", 16 * -1), command=popup.destroy)
    B1.pack()
    popup.mainloop()


show_frame(login_page)
root.mainloop()
