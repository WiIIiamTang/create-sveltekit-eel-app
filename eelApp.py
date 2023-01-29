import eel
import tkinter
from tkinter import filedialog as fd


eel.init("build", [".tsx", ".ts", ".jsx", ".js", ".html", ".svelte"])


@eel.expose
def hello_from_eel(name: str):
    print(f"Hello {name}, you are calling a function from Python")
    eel.hello_from_sk(name)


@eel.expose
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


print("Eel ws running on ws://localhost:8888")
eel.start("", size=(800, 600), port=8888, mode="chrome")
