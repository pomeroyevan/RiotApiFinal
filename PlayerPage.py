import tkinter as tk
import requests
from Player import player
from Consts import SummonerByName
from Consts import ProfileBYpuu


class PlayerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#333333")
        self.controller = controller

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self,
                              text="Player Username:",
                              fg="#99ccff",
                              bg="#333333",
                              font=("Helvetica", 12),
                              justify="center")
        self.label.grid(row=0, column=0, pady=10)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=0, pady=10)
        self.name_entry.focus()
        self.name_entry.bind("<Return>", lambda event: self.getUserName())

    def getUserName(self):
        UN = self.name_entry.get()
        userQ = SummonerByName(UN, key=self.controller.key)
        testQ = requests.get(userQ)
        if testQ.status_code == 200:
            self.player = player(UN, key=self.controller.key)
            self.syn = self.player.synergy()
            self.printSynergy()
        else:
            # print(userQ, testQ.json(), testQ.status_code)
            pass

    def printSynergy(self):
        R = 2
        for puu in self.syn:
            summonername = requests.get(
                ProfileBYpuu(puu, key=self.controller.key)).json().get(
                    'gameName')
            temp = tk.Label(self,
                            text=f"{
                                summonername} | games: {
                                    self.syn[puu][0]}  | avg place: {
                                        self.syn[puu][1]}",
                            fg="#99ccff",
                            bg="#333333",
                            font=("Helvetica", 12),
                            justify="left")
            temp.grid(row=R, column=0, pady=10)
            R += 1
