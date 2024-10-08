import tkinter as tk
import webbrowser
import requests


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#333333")
        self.controller = controller

        self.create_widgets()
        self.help_text = "Go to the Riot Developer Portal and login."\
                         "There you will find an API Key. Paste it here"\
                         "to access.\n\nNote: You must have a registered"\
                         "developer account with Riot Games."

    def create_widgets(self):
        """Create login page, buttons, and input field"""
        title_label = tk.Label(self,
                               text="Double Down TFT",
                               font=("Helvetica", 36),
                               fg="#99ccff",
                               bg="#333333")
        title_label.grid(row=0, column=0, pady=(75, 10))

        # Title
        subtitle_label = tk.Label(self,
                                  text="Advanced statistics for your TFT Duo",
                                  font=("Helvetica", 18),
                                  fg="#99ccff",
                                  bg="#333333")
        subtitle_label.grid(row=1, column=0, pady=10)

        # input field label
        api_label = tk.Label(self,
                             text="API Key:",
                             font=("Helvetica", 14),
                             fg="#99ccff",
                             bg="#333333")
        api_label.grid(row=3, column=0, pady=10)

        # input field for api key
        self.api_entry = tk.Entry(self, show='*', width=36)
        self.api_entry.grid(row=4, column=0, pady=10)
        self.api_entry.bind("<Return>", self.record_input)
        self.api_entry.focus()
        self.invalid_label = tk.Label(self,
                                      text="",
                                      font=("Helvetica", 12),
                                      fg="#CC0000",
                                      bg="#333333")
        self.invalid_label.grid(row=4, column=1, pady=10)

        # button link to riot api key help
        dev_link = tk.Label(self,
                            text="Riot Developer Portal ->",
                            fg="#99ccff",
                            bg="#333333",
                            cursor="hand2",
                            font=("Helvetica", 14))
        dev_link.bind("<Button-1>", self.open_riot_dev)
        dev_link.grid(row=5, column=0, pady=10)

        # button to display instructions
        help_link = tk.Label(self,
                             text="Need help?",
                             fg="#99ccff",
                             bg="#333333",
                             cursor="hand2",
                             font=("Helvetica", 12))

        help_link.bind("<Button-1>", self.show_help)
        help_link.grid(row=6, column=0, pady=10)

        # puts cursor in input field
        self.api_entry.focus()

    def open_riot_dev(self, event):
        """Searches web for riot developer support"""
        webbrowser.open("https://developer.riotgames.com/")

    def record_input(self, other):
        """Records inputed api key and displays next page"""
        api_key = self.api_entry.get()
        qString = f"https://americas.api.riotgames.com/riot/"\
                  f"account/v1/accounts/by-riot-id/thenucleartoast/"\
                  f"NA1?api_key={api_key}"
        testQ = requests.get(qString).status_code
        # if request is valid, continue to player page
        if testQ == 200:
            self.controller.key = api_key
            self.controller.show_page("SummonerSearch")
        else:
            # handle invalid api key
            self.invalid_label.config(text="Invalid API key")

    def show_help(self, event):
        """Display's instructions on screen"""
        self.help_label = tk.Label(self,
                                   text=self.help_text, fg="#99ccff",
                                   bg="#333333",
                                   font=("Helvetica", 12),
                                   justify="center")
        self.help_label.grid(row=7, column=0, pady=10)

    def badKey(self):
        """Displays feedback for invalid api key"""
        self.api_entry.delete(0, tk.END)
        self.invalid_label.config(text="Key not valid")
