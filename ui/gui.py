from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import ui.uiManager as uiManager


ASSETS_PATH = Path(r"assets/dashboard")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("937x667")
window.configure(bg = "#FFFFFF")


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


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
    95.84365844726562,
    332.84375,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    57.06329345703125,
    606.4606323242188,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    51.5494384765625,
    606.5604858398438,
    image=image_image_3
)

canvas.create_text(
    69.696044921875,
    599.2577514648438,
    anchor="nw",
    text="Logout",
    fill="#FFFFFF",
    font=("Poppins Regular", 10 * -1)
)

canvas.create_text(
    60.0,
    215.0,
    anchor="nw",
    text="Book Management",
    fill="#FFFFFF",
    font=("Poppins Regular", 10 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    64.302490234375,
    275.3021240234375,
    image=image_image_4
)

canvas.create_text(
    80.44921875,
    268.0,
    anchor="nw",
    text="Edit Profile",
    fill="#FFFFFF",
    font=("Poppins Regular", 10 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    61.0,
    175.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    45.0,
    223.486328125,
    image=image_image_6
)

canvas.create_text(
    77.44921875,
    166.0,
    anchor="nw",
    text="Dashboard",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 10 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    908.4921875,
    27.84375,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    561.0,
    117.00003051757812,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    658.0,
    115.0,
    image=image_image_9
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
    text="Welcome back, John!",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    791.2198486328125,
    135.65042114257812,
    image=image_image_10
)

canvas.create_text(
    204.0,
    201.0,
    anchor="nw",
    text="Available Books",
    fill="#000000",
    font=("Poppins SemiBold", 14 * -1)
)

my_rectangle = round_rectangle(
    204.0,
    241.0,
    917.0,
    646.0,
    radius=20,
    fill="#FFFFFF",
    width=3,
    outline="#925fe2")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    776.5,
    211.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F2F2F2",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=645.0,
    y=198.0,
    width=263.0,
    height=24.0
)
entry_1.insert(0, "Search Books")
entry_1.bind("<FocusIn>", lambda x: uiManager.on_entry_focus_in(entry_1, "Search Books"))
entry_1.bind("<FocusOut>", lambda x: uiManager.on_entry_focus_out(entry_1, "Search Books"))

window.resizable(False, False)
window.mainloop()
