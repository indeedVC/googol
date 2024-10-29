import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")

        self.title("Googol")
        self.geometry("600x400")
        self.minsize(300, 200)
