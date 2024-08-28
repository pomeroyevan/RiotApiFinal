import tkinter as tk
import webbrowser
import requests

class DoubleDownTFT(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Double Down TFT")
        self.geometry("800x600")
        self.configure(bg="#333333")  # Darker background color

        self.container = tk.Frame(self, bg="#333333")
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        self.pages = {}

        # Create and add pages
        page = LoginPage(parent=self.container, controller=self)
        self.pages["LoginPage"] = page
        page.grid(row=0, column=0, sticky="nsew")
        self.show_page("LoginPage")

        next_page = NextPage(parent=self.container, controller=self)
        self.pages["NextPage"] = next_page
        next_page.grid(row=0, column=0, sticky="nsew")

        self.show_page("LoginPage")

    def show_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#333333")
        self.controller = controller

        self.create_widgets()
        self.help_text = "Go to the Riot Developer Portal and login. There you will find an API Key. Paste it here to access.\n\nNote: You must have a registered developer account with Riot Games."

    def create_widgets(self):
        title_label = tk.Label(self, text="Double Down TFT", font=("Helvetica", 36), fg="#99ccff", bg="#333333")
        title_label.place(relx=0.5 , rely=0.1, anchor="center")

        subtitle_label = tk.Label(self, text="Advanced statistics for your TFT Duo", font=("Helvetica", 18), fg="#99ccff", bg="#333333")
        subtitle_label.place(relx=0.5, rely=0.2, anchor="center")

        api_label = tk.Label(self, text="API Key:", font=("Helvetica", 14), fg="#99ccff", bg="#333333")
        api_label.place(relx=0.3, rely=0.6, anchor="center")

        self.api_entry = tk.Entry(self, show='*', width=36)
        self.api_entry.place(relx=0.5, rely=0.6, anchor="center")
        self.api_entry.focus()

        self.invalid_label = tk.Label(self, text="", font=("Helvetica", 12), fg="#CC0000", bg="#333333")
        self.invalid_label.place(relx=.36, rely=.62)

        dev_link = tk.Label(self, text="Riot Developer Portal ->", fg="#99ccff", bg="#333333", cursor="hand2", font=("Helvetica", 14))
        dev_link.bind("<Button-1>", self.open_riot_dev)
        dev_link.place(relx=0.5, rely=0.4, anchor="center")

        self.help_label = tk.Label(self, text='', fg="#99ccff", bg="#333333", font=("Helvetica", 12), justify="center")
        self.help_label.place(relx=0.5, rely=0.8, anchor="center")

        help_link = tk.Label(self, text="Need help?", fg="#99ccff", bg="#333333", cursor="hand2", font=("Helvetica", 12))
        help_link.place(relx=0.59, rely=0.55, anchor="center")

    def open_riot_dev(self, event):
        webbrowser.open("https://developer.riotgames.com/")

    def record_input(self):
        api_key = self.api_entry.get()
        testQ = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/thenucleartoast?api_key={api_key}').status_code
        if testQ == 200:
            self.controller.show_page("NextPage")
        else:
            self.invalid_label.config(text="Invalid API key")

    def show_help(self, event):
        self.help_label.config(text= self.help_text)

class NextPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#333333")
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Next Page Content", font=("Helvetica", 24), fg="#99ccff", bg="#333333")
        label.pack(anchor="center")

if __name__ == "__main__":
    app = DoubleDownTFT()
    app.mainloop()
