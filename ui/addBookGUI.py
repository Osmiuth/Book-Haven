from pathlib import Path
from tkinter import Canvas, Text, Button, PhotoImage, Frame

ASSETS_PATH = Path(r"ui/assets/bookManage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_book_gui_start(root):
    add_book_gui = Frame(root)
    add_book_gui.pack(fill="both", expand=True)

    canvas = Canvas(
        add_book_gui,
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

    submit_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    submit_button = Button(
        add_book_gui,
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
        229.0,
        91.0,
        anchor="nw",
        text="Book Name:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        229.0,
        147.0,
        anchor="nw",
        text="Author:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        229.0,
        436.0,
        anchor="nw",
        text="Price: ",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        493.0,
        436.0,
        anchor="nw",
        text="Stock:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        229.0,
        195.0,
        anchor="nw",
        text="Book Description:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        229.0,
        377.0,
        anchor="nw",
        text="Genre:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        593.0,
        91.0,
        anchor="nw",
        text="ISBN:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    canvas.create_text(
        593.0,
        147.0,
        anchor="nw",
        text="Date Published:",
        fill="#925FE2",
        font=("Poppins SemiBold", 11 * -1)
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        94.0,
        333.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        55.219635009765625,
        606.6168823242188,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        49.705780029296875,
        606.7167358398438,
        image=image_image_5
    )

    canvas.create_text(
        67.85238647460938,
        599.4140014648438,
        anchor="nw",
        text="Logout",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    add_books_button = Button(
        add_book_gui,
        borderwidth=0,
        highlightthickness=0,
        background="#925FE2",
        activebackground="#925FE2",
        foreground="#FFFFFF",
        text="Add Books",
        font=("Poppins SemiBold", 10 * -1)
    )
    add_books_button.place(
        x=75,
        y=215.15625,
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        59,
        275.4583740234375,
        image=image_image_6
    )

    edit_user_profile_button = Button(
        add_book_gui,
        borderwidth=0,
        highlightthickness=0,
        background="#925FE2",
        activebackground="#925FE2",
        foreground="#DEDEDE",
        text="Edit Profile",
        font=("Poppins SemiBold", 10 * -1)
    )
    edit_user_profile_button.place(
        x=75,
        y=268.15625,
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        59.156341552734375,
        175.15625,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        59,
        223.642578125,
        image=image_image_8
    )

    dashboard_button = Button(
        add_book_gui,
        borderwidth=0,
        highlightthickness=0,
        background="#925FE2",
        activebackground="#925FE2",
        foreground="#DEDEDE",
        text="Dashboard",
        font=("Poppins SemiBold", 10 * -1)
    )
    dashboard_button.place(
        x=75.60556030273438,
        y=166.15625,
    )

    book_name_entry_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    book_name_entry_bg = canvas.create_image(
        440.5,
        109.0,
        image=book_name_entry_image
    )
    book_name_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_name_entry.place(
        x=325.0,
        y=89.0,
        width=231.0,
        height=28.0
    )

    author_entry_image = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    author_entry_bg = canvas.create_image(
        440.5,
        165.0,
        image=author_entry_image
    )
    author_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    author_entry.place(
        x=325.0,
        y=146.0,
        width=231.0,
        height=28.0
    )

    isbn_entry_image = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    isbn_entry_bg = canvas.create_image(
        768.0,
        109.0,
        image=isbn_entry_image
    )
    isbn_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    isbn_entry.place(
        x=649.0,
        y=92.0,
        width=238.0,
        height=27.0
    )

    date_published_entry_image = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    date_published_entry_bg = canvas.create_image(
        797.0,
        165.0,
        image=date_published_entry_image
    )
    date_published_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    date_published_entry.place(
        x=707.0,
        y=148.0,
        width=180.0,
        height=27.0
    )

    genre_entry_image = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    genre_entry_bg = canvas.create_image(
        385.5,
        395.0,
        image=genre_entry_image
    )
    genre_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    genre_entry.place(
        x=290.0,
        y=378.0,
        width=191.0,
        height=26.0
    )

    price_entry_image = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    price_entry_bg = canvas.create_image(
        314.0,
        454.0,
        image=price_entry_image
    )
    price_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    price_entry.place(
        x=290.0,
        y=437.0,
        width=48.0,
        height=27.0
    )

    stock_entry_image = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    stock_entry_bg = canvas.create_image(
        579.0,
        454.0,
        image=stock_entry_image
    )
    stock_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    stock_entry.place(
        x=555.0,
        y=437.0,
        width=48.0,
        height=27.0
    )

    book_description_entry_image = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    book_description_entry_bg = canvas.create_image(
        564.0,
        291.0,
        image=book_description_entry_image
    )
    book_description_entry = Text(
        add_book_gui,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    book_description_entry.place(
        x=245.0,
        y=227.0,
        width=638.0,
        height=120.0
    )

    add_book_gui.image_image_1 = image_image_1
    add_book_gui.image_image_2 = image_image_2
    add_book_gui.submit_button_image = submit_button_image
    add_book_gui.image_image_3 = image_image_3
    add_book_gui.image_image_4 = image_image_4
    add_book_gui.image_image_5 = image_image_5
    add_book_gui.image_image_6 = image_image_6
    add_book_gui.image_image_7 = image_image_7
    add_book_gui.image_image_8 = image_image_8
    add_book_gui.book_name_entry = book_name_entry
    add_book_gui.author_entry = author_entry
    add_book_gui.isbn_entry = isbn_entry
    add_book_gui.date_published_entry = date_published_entry
    add_book_gui.genre_entry = genre_entry
    add_book_gui.price_entry = price_entry
    add_book_gui.stock_entry = stock_entry
    add_book_gui.book_description_entry = book_description_entry
    add_book_gui.book_name_entry_image = book_name_entry_image
    add_book_gui.author_entry_image = author_entry_image
    add_book_gui.isbn_entry_image = isbn_entry_image
    add_book_gui.date_published_entry_image = date_published_entry_image
    add_book_gui.genre_entry_image = genre_entry_image
    add_book_gui.price_entry_image = price_entry_image
    add_book_gui.stock_entry_image = stock_entry_image
    add_book_gui.book_description_entry_image = book_description_entry_image

    add_book_gui.dashboard_button = dashboard_button
    add_book_gui.add_books_button = add_books_button
    add_book_gui.submit_button = submit_button
    add_book_gui.edit_user_profile_button = edit_user_profile_button

    return add_book_gui
