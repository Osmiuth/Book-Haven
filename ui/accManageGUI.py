from pathlib import Path
from tkinter import Canvas, Text, Button, PhotoImage, Frame

ASSETS_PATH = Path(r"ui/assets/accManage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def acc_management_gui_start(root):
    acc_management_gui = Frame(root)
    acc_management_gui.pack(fill="both", expand=True)

    canvas = Canvas(
        acc_management_gui,
        bg = "#FFFFFF",
        height = 667,
        width = 937,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.pack()
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        908.4921875,
        27.84375,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        560.0,
        356.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        559.0,
        161.0,
        image=image_image_3
    )

    name = canvas.create_text(
        231.0,
        90.0,
        anchor="nw",
        text="Galendez, \nClint Jonathan A.",
        fill="#020000",
        font=("Poppins SemiBold", 40 * -1)
    )

    canvas.create_text(
        772.0,
        184.0,
        anchor="nw",
        text="Account Management",
        fill="#000000",
        font=("Poppins Regular", 10 * -1)
    )

    submit_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    submit_button = Button(
        acc_management_gui,
        image=submit_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    submit_button.place(
        x=694.0,
        y=601.0,
        width=198.0,
        height=25.81640625
    )

    canvas.create_text(
        226.0,
        341.0,
        anchor="nw",
        text="New Username:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        590.0,
        285.0,
        anchor="nw",
        text="Current Password:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        590.0,
        341.0,
        anchor="nw",
        text="New Password:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        94.0,
        333.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        55.219635009765625,
        606.6168823242188,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        49.705780029296875,
        606.7167358398438,
        image=image_image_6
    )

    canvas.create_text(
        67.85238647460938,
        599.4140014648438,
        anchor="nw",
        text="Logout",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    canvas.create_text(
        58.156341552734375,
        215.15625,
        anchor="nw",
        text="Book Management",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        62.458831787109375,
        275.4583740234375,
        image=image_image_7
    )

    canvas.create_text(
        78.60556030273438,
        268.15625,
        anchor="nw",
        text="Edit Profile",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        59.156341552734375,
        175.15625,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        43.156341552734375,
        223.642578125,
        image=image_image_9
    )

    canvas.create_text(
        75.60556030273438,
        166.15625,
        anchor="nw",
        text="Dashboard",
        fill="#FFFFFF",
        font=("Poppins SemiBold", 10 * -1)
    )

    new_password_entry_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    new_password_entry_bg = canvas.create_image(
        445.0,
        359.0,
        image=new_password_entry_image
    )
    new_password_entry = Text(
        acc_management_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    new_password_entry.place(
        x=344.0,
        y=340.0,
        width=202.0,
        height=22.0
    )

    current_password_entry_image = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    current_password_entry_bg = canvas.create_image(
        801.0,
        303.0,
        image=current_password_entry_image
    )
    current_password_entry = Text(
        acc_management_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    current_password_entry.place(
        x=718.0,
        y=286.0,
        width=166.0,
        height=22.0
    )

    new_username_entry_image = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    new_username_entry_bg = canvas.create_image(
        801.0,
        359.0,
        image=new_username_entry_image
    )
    new_username_entry = Text(
        acc_management_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    new_username_entry.place(
        x=718.0,
        y=342.0,
        width=166.0,
        height=22.0
    )

    acc_management_gui.image_image_1 = image_image_1
    acc_management_gui.image_image_2 = image_image_2
    acc_management_gui.image_image_3 = image_image_3
    acc_management_gui.submit_button_image = submit_button_image
    acc_management_gui.image_image_4 = image_image_4
    acc_management_gui.image_image_5 = image_image_5
    acc_management_gui.image_image_6 = image_image_6
    acc_management_gui.image_image_7 = image_image_7
    acc_management_gui.image_image_8 = image_image_8
    acc_management_gui.image_image_9 = image_image_9
    acc_management_gui.new_password_entry_image = new_password_entry_image
    acc_management_gui.current_password_entry_image = current_password_entry_image
    acc_management_gui.new_username_entry_image = new_username_entry_image

    acc_management_gui.new_password_entry = new_password_entry
    acc_management_gui.current_password_entry = current_password_entry
    acc_management_gui.new_username_entry = new_username_entry
    acc_management_gui.name = name
    acc_management_gui.submit_button = submit_button

    return acc_management_gui
