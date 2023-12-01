from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
import ui.uiManager as uiManager


ASSETS_PATH = Path(r"ui/assets/login")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_gui_start(root):
    login_gui = Frame(root)
    login_gui.pack(fill="both", expand=True)

    canvas = Canvas(
        login_gui,
        bg = "#925FE2",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.pack()
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
        login_gui,
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

    username_entry_image = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    username_textbox_background = canvas.create_image(
        309.0,
        363.5,
        image=username_entry_image
    )
    username_entry = Entry(
        login_gui,
        bd=0,
        bg="#1C1D21",
        fg="white",
        highlightthickness=0
    )
    username_entry.place(
        x=119.0,
        y=345.0,
        width=380.0,
        height=35.0
    )
    username_entry.insert(0, "Username")
    username_entry.bind("<FocusIn>", lambda x: uiManager.on_entry_focus_in(username_entry, "Username"))
    username_entry.bind("<FocusOut>", lambda x: uiManager.on_entry_focus_out(username_entry, "Username"))

    password_entry_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    password_textbox_background = canvas.create_image(
        309.0,
        422.5,
        image=password_entry_image
    )
    password_entry = Entry(
        login_gui,
        bd=0,
        bg="#1C1D21",
        fg="white",
        show="*",
        highlightthickness=0
    )
    password_entry.place(
        x=119.0,
        y=404.0,
        width=380.0,
        height=35.0
    )
    password_entry.insert(0, "Password")
    password_entry.bind("<FocusIn>", lambda x: uiManager.on_entry_focus_in(password_entry, "Password"))
    password_entry.bind("<FocusOut>", lambda x: uiManager.on_entry_focus_out(password_entry, "Password"))

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1024.0,
        500.0,
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

    login_gui.submit_button_image_1 = submit_button_image_1
    login_gui.username_textbox_image = username_entry_image
    login_gui.password_textbox_image = password_entry_image
    login_gui.image_image_1 = image_image_1

    login_gui.username_entry = username_entry
    login_gui.password_entry = password_entry
    login_gui.submit_button = submit_button

    return login_gui
