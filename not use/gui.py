import tkinter as tk
import requests as r
import webbrowser

# Function to handle button click event
def update_entry():
    text = api_entry.get()
    if len(text) > 42:
        badKey()
    if len(text) == 42:
        record_input()
    api_entry.after(100, update_entry)


def record_input():
    api_key = api_entry.get()
    testQ = r.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/thenucleartoast?api_key={api_key}').status_code
    if testQ == 200:
        return
    else:
        badKey()

def open_riot_dev():
    webbrowser.open("https://developer.riotgames.com/")
        

def badKey(): 
    invalid_label.config(text="Invalid API key")
    api_entry.delete(0, tk.END)

def helping_login():
    help_login.config(text='Go to the Riot Developer Portal and login.  There you will find an API Key. Paste it here to access.\n\nNote: You must have a registered developer account with Riot Games.')


# Create the main window
window = tk.Tk()
window.title("Double Down TFT")
window.geometry("800x600")
window.configure(bg="#333333")  # Darker background color

# Create a label with large text in the top middle
title_label = tk.Label(window, text="Double Down TFT", font=("Helvetica", 36), fg="#99ccff", bg="#333333")  # Lighter text color
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Create a label with smaller text below the title
subtitle_label = tk.Label(window, text="Advanced statistics for your TFT Duo", font=("Helvetica", 18), fg="#99ccff", bg="#333333")  # Lighter text color
subtitle_label.place(relx=0.5, rely=0.2, anchor="center")

# Create a label for the API key input
api_label = tk.Label(window, text="API Key:", font=("Helvetica", 14), fg="#99ccff", bg="#333333")  # Lighter text color
api_label.place(relx=0.3, rely=0.6, anchor="center")

# Create an entry field for API key input
api_entry = tk.Entry(window, show ='*', width=36)
api_entry.place(relx=0.5, rely=0.6, anchor="center")
api_entry.focus()

# Create a button with question mark
question_button = tk.Button(window, text="?", font=("Helvetica", 14), fg="#99ccff", bg="#333333", width=2, height=1, bd=0)  # Circular button
question_button.place(relx=.98, rely=0.03, anchor="center")


invalid_label = tk.Label(window, text="",font=("Helvetica", 12), fg="#CC0000", bg="#333333")
invalid_label.place(relx=.36, rely=.62)

dev_link = tk.Label(window, text="Riot Developer Portal ->", fg="#99ccff", bg="#333333", cursor="hand2", font=("Helvetica", 14))
dev_link.pack(pady=5)
dev_link.place(relx=0.5, rely=0.4, anchor="center")
dev_link.bind("<Button-1>", lambda event: open_riot_dev())

help_link = tk.Label(window, text="Need help?", fg="#99ccff", bg="#333333", cursor="hand2", font=("Helvetica", 12))
help_link.pack(pady=5)
help_link.place(relx=0.59, rely=0.55, anchor="center")
help_link.bind("<Button-1>", lambda event: helping_login())

help_login = tk.Label(window, text="", fg="#99ccff", bg="#333333", cursor="hand2", font=("Helvetica", 12))
help_login.pack(pady=5)
help_login.place(relx=0.5, rely=0.8, anchor="center")

# Run the Tkinter event loop
update_entry()

window.mainloop()
