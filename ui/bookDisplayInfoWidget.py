import tkinter
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame


ASSETS_PATH = Path(r"ui/assets/bookDisplayInfo")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class BookDisplayInfoWidget(Frame):
    def __init__(self, parent, book_title, author, date_added, stock, price):
        Frame.__init__(self, parent, bg="#925FE2", borderwidth=4, border=1)

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 146,
            width = 330,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.pack()
        self.canvas.create_text(
            140.0,
            55.0,
            anchor="nw",
            text="Author:",
            fill="#925FE2",
            font=("Poppins SemiBold", 11 * -1)
        )

        self.canvas.create_text(
            140.0,
            73.0,
            anchor="nw",
            text="Date Added:",
            fill="#925FE2",
            font=("Poppins SemiBold", 11 * -1)
        )

        self.book_title_text = self.canvas.create_text(
            140.0,
            17.0,
            anchor="nw",
            text="Book Title",
            fill="#020000",
            font=("Poppins SemiBold", 24 * -1)
        )

        self.author_text = self.canvas.create_text(
            193.7310791015625,
            55.0,
            anchor="nw",
            text="Author",
            fill="#000000",
            font=("Poppins Regular", 10 * -1)
        )

        self.date_added_text = self.canvas.create_text(
            219.7310791015625,
            73.0,
            anchor="nw",
            text="Date Added",
            fill="#000000",
            font=("Poppins Regular", 10 * -1)
        )

        self.stock_text = self.canvas.create_text(
            185.7310791015625,
            91.0,
            anchor="nw",
            text="Stock",
            fill="#000000",
            font=("Poppins Regular", 10 * -1)
        )

        self.price_text = self.canvas.create_text(
            184.7310791015625,
            108.0,
            anchor="nw",
            text="Price",
            fill="#000000",
            font=("Poppins Regular", 10 * -1)
        )

        self.canvas.create_text(
            140.0,
            91.0,
            anchor="nw",
            text="Stock:",
            fill="#925FE2",
            font=("Poppins SemiBold", 11 * -1)
        )

        self.canvas.create_text(
            140.0,
            108.0,
            anchor="nw",
            text="Price: ",
            fill="#925FE2",
            font=("Poppins SemiBold", 11 * -1)
        )

        self.edit_book_button_image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.edit_book_button = Button(
            self,
            image=self.edit_book_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.edit_book_button.place(
            x=19.0,
            y=17.0,
            width=106.0,
            height=52.0
        )

        self.delete_book_button_image = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.delete_book_button = Button(
            self,
            image=self.delete_book_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.delete_book_button.place(
            x=19.0,
            y=77.0,
            width=106.0,
            height=52.0
        )

        self.canvas.itemconfig(self.book_title_text, text=book_title)
        self.canvas.itemconfig(self.author_text, text=author)
        self.canvas.itemconfig(self.date_added_text, text=date_added)
        self.canvas.itemconfig(self.stock_text, text=stock)
        self.canvas.itemconfig(self.price_text, text=price)