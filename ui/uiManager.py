def on_entry_focus_in(textbox, placeholder):
    if textbox.get() == placeholder:
        textbox.delete(0, "end")


def on_entry_focus_out(textbox, placeholder):
    if textbox.get() == "":
        textbox.insert(0, placeholder)