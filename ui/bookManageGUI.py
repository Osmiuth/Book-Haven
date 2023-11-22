from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import ui.uiManager as uiManager

ASSETS_PATH = Path(r"assets/bookManage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("937x667")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 667,
    width = 937,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
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

canvas.create_text(
    58.156341552734375,
    215.15625,
    anchor="nw",
    text="Book Management",
    fill="#FFFFFF",
    font=("Poppins Regular", 10 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    62.458831787109375,
    275.4583740234375,
    image=image_image_6
)

canvas.create_text(
    78.60556030273438,
    268.15625,
    anchor="nw",
    text="Edit Profile",
    fill="#FFFFFF",
    font=("Poppins Regular", 10 * -1)
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
    43.156341552734375,
    223.642578125,
    image=image_image_8
)

canvas.create_text(
    75.60556030273438,
    166.15625,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 10 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    440.5,
    109.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=325.0,
    y=89.0,
    width=231.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    440.5,
    165.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=325.0,
    y=146.0,
    width=231.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    768.0,
    109.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=649.0,
    y=92.0,
    width=238.0,
    height=27.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    797.0,
    165.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=707.0,
    y=148.0,
    width=180.0,
    height=27.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    385.5,
    395.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=290.0,
    y=378.0,
    width=191.0,
    height=26.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    314.0,
    454.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=290.0,
    y=437.0,
    width=48.0,
    height=27.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    579.0,
    454.0,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=555.0,
    y=437.0,
    width=48.0,
    height=27.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    564.0,
    291.0,
    image=entry_image_8
)
entry_8 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=245.0,
    y=227.0,
    width=638.0,
    height=120.0
)
window.resizable(False, False)
window.mainloop()