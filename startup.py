import tkinter as tk
from loginPage import LoginPage
from PlayerPage import PlayerPage


class DoubleDownTFT(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Double Down TFT")
        self.geometry("800x600")
        self.configure(bg="#333333")  # Darker background color

        self.container = tk.Frame(self, bg="#333333")
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        self.key = ''

        self.pages = {}

        # Create and add pages
        page = LoginPage(parent=self.container, controller=self)
        self.pages["LoginPage"] = page
        page.grid(row=0, column=0, sticky="nsew") 

        next_page = PlayerPage(parent=self.container, controller=self)
        self.pages["PlayerPage"] = next_page
        next_page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()


if __name__ == "__main__":
    app = DoubleDownTFT()
    app.mainloop()
