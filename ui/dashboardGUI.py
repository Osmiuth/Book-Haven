from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, Frame, Button
import ui.uiManager as uiManager
import ui.bookDisplayInfoWidget as bookDisplayInfoWidget



ASSETS_PATH = Path(r"ui/assets/dashboard")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


firstName = "Clint"


def dashboard_gui_start(root):
    global firstName

    dashboard_gui = Frame(root)
    dashboard_gui.pack(fill="both", expand=True)

    canvas = Canvas(
        dashboard_gui,
        bg = "#FFFFFF",
        height = 667,
        width = 937,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.pack()
    side_board_image = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        95.84365844726562,
        332.84375,
        image=side_board_image
    )

    logout_image_set_1 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        57.06329345703125,
        606.4606323242188,
        image=logout_image_set_1
    )

    logout_image_set_2 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        51.5494384765625,
        606.5604858398438,
        image=logout_image_set_2
    )

    canvas.create_text(
        69.696044921875,
        599.2577514648438,
        anchor="nw",
        text="Logout",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    add_books_button = Button(
        dashboard_gui,
        borderwidth=0,
        highlightthickness=0,
        background="#925FE2",
        activebackground="#925FE2",
        foreground="#DEDEDE",
        text="Add Books",
        font=("Poppins SemiBold", 10 * -1)
    )
    add_books_button.place(
        x=75,
        y=215.15625,
    )

    edit_profile_image = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        59,
        275.3021240234375,
        image=edit_profile_image
    )

    edit_user_profile_button = Button(
        dashboard_gui,
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

    dashboard_image = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        61.0,
        175.0,
        image=dashboard_image
    )

    book_management_image = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        59,
        223.486328125,
        image=book_management_image
    )

    dashboard_button = Button(
        dashboard_gui,
        borderwidth=0,
        highlightthickness=0,
        background="#925FE2",
        activebackground="#925FE2",
        foreground="#FFFFFF",
        text="Dashboard",
        font=("Poppins SemiBold", 10 * -1)
    )
    dashboard_button.place(
        x=75.60556030273438,
        y=166.15625,
    )

    notification_image = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        908.4921875,
        27.84375,
        image=notification_image
    )

    header_image = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        561.0,
        117.00003051757812,
        image=header_image
    )

    graduation_image = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        658.0,
        115.0,
        image=graduation_image
    )

    canvas.create_text(
        244.30859375,
        89.64065551757812,
        anchor="nw",
        text="September 4,  2023",
        fill="#FFFFFF",
        font=("Poppins Regular", 10 * -1)
    )

    canvas.create_text(
        242.0,
        113.00003051757812,
        anchor="nw",
        text="Welcome back, " + firstName + "!",
        fill="#FFFFFF",
        font=("Poppins SemiBold", 20 * -1)
    )

    backpack_image = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        791.2198486328125,
        135.65042114257812,
        image=backpack_image
    )

    canvas.create_text(
        204.0,
        201.0,
        anchor="nw",
        text="Available Books",
        fill="#000000",
        font=("Poppins SemiBold", 14 * -1)
    )

    book_list_canvas = uiManager.round_rectangle(
        canvas,
        204.0,
        241.0,
        917.0,
        646.0,
        radius=20,
        fill="#FFFFFF",
        width=3,
        outline="#925fe2")

    search_entry_image = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    search_entry_bg = canvas.create_image(
        776.5,
        211.0,
        image=search_entry_image
    )
    search_entry = Entry(
        dashboard_gui,
        bd=0,
        bg="#F2F2F2",
        fg="#000716",
        highlightthickness=0
    )
    search_entry.place(
        x=645.0,
        y=198.0,
        width=263.0,
        height=24.0
    )
    search_entry.insert(0, "Search Books")
    search_entry.bind("<FocusIn>", lambda x: uiManager.on_entry_focus_in(search_entry, "Search Books"))
    search_entry.bind("<FocusOut>", lambda x: uiManager.on_entry_focus_out(search_entry, "Search Books"))

    book_list_frame = Frame(
        dashboard_gui,
        width=700,
        height=399,
        borderwidth=1,
        bg="#FFFFFF",
    )
    book_list_frame.place(
        x=211,
        y=245
    )

    book1 = bookDisplayInfoWidget.BookDisplayInfoWidget(
        parent=book_list_frame,
        book_title="Book Name",
        author="Author",
        date_added="Date Added",
        stock="Stock",
        price="Price",
    )
    book1.grid(row=0, column=0, padx=10, pady=10)

    book2 = bookDisplayInfoWidget.BookDisplayInfoWidget(
        parent=book_list_frame,
        book_title="Book Name",
        author="Author",
        date_added="Date Added",
        stock="Stock",
        price="Price",
    )
    book2.grid(row=0, column=1, padx=10, pady=10)

    dashboard_gui.side_board_image = side_board_image
    dashboard_gui.logout_image_set_1 = logout_image_set_1
    dashboard_gui.logout_image_set_2 = logout_image_set_2
    dashboard_gui.edit_profile_image = edit_profile_image
    dashboard_gui.dashboard_image = dashboard_image
    dashboard_gui.book_management_image = book_management_image
    dashboard_gui.notification_image = notification_image
    dashboard_gui.header_image = header_image
    dashboard_gui.graduation_image = graduation_image
    dashboard_gui.backpack_image = backpack_image
    dashboard_gui.search_box_image = search_entry_image

    dashboard_gui.search_entry = search_entry

    dashboard_gui.book_list_frame = book_list_frame

    dashboard_gui.dashboard_button = dashboard_button
    dashboard_gui.add_books_button = add_books_button
    dashboard_gui.edit_user_profile_button = edit_user_profile_button
    dashboard_gui.book_list_canvas = book_list_canvas

    dashboard_gui.firstName = firstName

    return dashboard_gui
