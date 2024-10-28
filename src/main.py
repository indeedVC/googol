#import tkinter
import customtkinter
from numba import jit
#from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("GOOGOL")
root.geometry("600x400")
#root.wm_iconphoto(True, ImageTk.PhotoImage(Image.open("assets/icon.png")))

if __name__ == "__main__":
    root.mainloop()