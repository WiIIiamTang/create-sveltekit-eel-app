import tkinter
from tkinter import filedialog as fd
import logging
import eel


def choose_file() -> str:
    tkinter.Tk().withdraw()
    root = tkinter.Tk()
    root.attributes("-alpha", 0.0)
    root.attributes("-topmost", True)
    filename = fd.askopenfilename(
        parent=root, title="Choose a file", filetypes=[("All files", "*.*")]
    )
    root.destroy()
    return filename


def hello_from_eel(name: str):
    logging.info(f"Hello from eel, {name}!")
    eel.hello_from_sk("World")
