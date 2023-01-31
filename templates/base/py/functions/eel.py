"""
Any callable in this file will be automatically exposed to eel at runtime.
Write everything you need here.
"""
import tkinter
from tkinter import filedialog as fd
import logging
import eel
import requests


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


def get_data() -> list:
    url = "https://dummyjson.com/products?limit=10"
    try:
        response = requests.get(url)
        eel.sleep(2)
        return response.json().get("products")
    except Exception as e:
        logging.error(f"Failed to get data from {url}")
        logging.error(e)
        return []
