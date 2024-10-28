from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("GOOGOL")
root.geometry("600x400")
root.wm_iconphoto(True, ImageTk.PhotoImage(Image.open("assets/icon.png")))

if __name__ == "__main__":
    root.mainloop()