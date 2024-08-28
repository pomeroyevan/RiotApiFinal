import tkinter as tk
from loginPage import LoginPage
from PlayerPage import PlayerPage


class DoubleDownTFT(tk.Tk):
    """UI Window Startup"""
    def __init__(self):
        """Initialize windo and gui"""
        tk.Tk.__init__(self)
        self.title("Double Down TFT")
        self.geometry("800x600")
        self.configure(bg="#333333")  # Darker background color
        self.container = tk.Frame(self, bg="#333333")
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        self.key = ''
        self.pages = {}

        # Create login page
        page = LoginPage(parent=self.container, controller=self)
        self.pages["LoginPage"] = page
        page.grid(row=0, column=0, sticky="nsew")

        # Create player page
        next_page = PlayerPage(parent=self.container, controller=self)
        self.pages["PlayerPage"] = next_page
        next_page.grid(row=0, column=0, sticky="nsew")

        # Show the login page
        self.show_page("LoginPage")

    def show_page(self, page_name):
        """
        Changes page of UI
        Args:
            page_name     -- Name of next page
        """
        page = self.pages[page_name]
        page.tkraise()


if __name__ == "__main__":
    # Begin
    app = DoubleDownTFT()
    app.mainloop()
