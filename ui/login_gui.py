from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def on_entry_focus_in(textbox, placeholder):
    if textbox.get() == placeholder:
        textbox.delete(0, "end")


def on_entry_focus_out(textbox, placeholder):
    if textbox.get() == "":
        textbox.insert(0, placeholder)


ASSETS_PATH = Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1280x720")
window.configure(bg = "#925FE2")


canvas = Canvas(
    window,
    bg = "#925FE2",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    630.0,
    720.0,
    fill="#1C1D21",
    outline="")

# Button Design Parameter
submit_button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
# Button Initialization
submit_button = Button(
    image=submit_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
submit_button.place(
    x=119.0,
    y=494.0,
    width=393.0,
    height=48.0
)

# Text "Login" Design Parameter
canvas.create_text(
    119.0,
    194.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Poppins Bold", 48 * -1)
)
#
canvas.create_text(
    119.0,
    278.0,
    anchor="nw",
    text="Enter your account details",
    fill="#FFFFFF",
    font=("Poppins Medium", 16 * -1)
)

username_textbox_image = PhotoImage(
    file=relative_to_assets("entry_2.png"))
username_textbox_background = canvas.create_image(
    309.0,
    363.5,
    image=username_textbox_image
)
username_textbox = Entry(
    bd=0,
    bg="#1C1D21",
    fg="white",
    highlightthickness=0
)
username_textbox.place(
    x=119.0,
    y=345.0,
    width=380.0,
    height=35.0
)
username_textbox.insert(0, "Username")
username_textbox.bind("<FocusIn>", lambda x: on_entry_focus_in(username_textbox, "Username"))
username_textbox.bind("<FocusOut>", lambda x: on_entry_focus_out(username_textbox, "Username"))

password_textbox_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
password_textbox_background = canvas.create_image(
    309.0,
    422.5,
    image=password_textbox_image
)
password_textbox = Entry(
    bd=0,
    bg="#1C1D21",
    fg="white",
    highlightthickness=0
)
password_textbox.place(
    x=119.0,
    y=404.0,
    width=380.0,
    height=35.0
)
password_textbox.insert(0, "Password")
password_textbox.bind("<FocusIn>", lambda x: on_entry_focus_in(password_textbox, "Password"))
password_textbox.bind("<FocusOut>", lambda x: on_entry_focus_out(password_textbox, "Password"))

canvas.create_text(
    633.0,
    230.0,
    anchor="nw",
    text=" Portal",
    fill="#EEEEEE",
    font=("Poppins Bold", 80 * -1)
)

canvas.create_text(
    650.0,
    155.0,
    anchor="nw",
    text="Bookhaven ",
    fill="#EEEEEE",
    font=("Poppins Bold", 80 * -1)
)

canvas.create_text(
    655.0,
    327.0,
    anchor="nw",
    text="Login to access your account",
    fill="#EEEEEE",
    font=("Poppins Medium", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1024.0,
    682.0,
    image=image_image_1
)

canvas.create_rectangle(
    118.0,
    385.0,
    500.0,
    386.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    118.0,
    445.0,
    500.0,
    446.0,
    fill="#FFFFFF",
    outline="")


def get_username_text():
    """
    get_username_text returns the text in the username textbox
    :return: username_textbox.get()
    """
    return username_textbox.get()


def get_password_text():
    """
    get_password_text returns the text in the password textbox
    :return: password_textbox.get()
    """
    return password_textbox.get()


def get_submit_button():
    """
    get_submit_button returns the submit button
    :return: submit_button
    """
    return submit_button


def error_message(msg):
    """
    error_message creates a popup window with the error message msg
    :param msg: the message to be displayed
    :return: None
    """
    popup = Tk()
    popup.wm_title("!")
    popup.geometry("300x100")
    popup.configure(bg="#925FE2")
    label = Text(popup, text=msg, bg="#925FE2", fg="white", font=("Poppins Medium", 16 * -1))
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#1C1D21", fg="white", font=("Poppins Medium", 16 * -1), command=popup.destroy)
    B1.pack()
    popup.mainloop()


window.resizable(False, False)
window.title("Log In")
window.mainloop()
