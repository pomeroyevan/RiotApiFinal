import requests as r
from Consts import SummonerByName, GamesByPUU
from Match import match
import json
from tkinter import filedialog


class player:

    def getGames(self):  # get's list of game IDs
        games = r.get(GamesByPUU(self.puu, key=self.key)).json()
        return games

    def makeMatchList(self):
        matches = {}
        for game in self.games:
            newm = match(game, key=self.key)
            if f"{newm.raw.get('info').get('tft_game_type')}" == 'pairs':
                matches.update({game: newm}) 
                # creates match objects from gameIDs in dictionary
        return matches

    def getRaw(self):  # get player profile from player name
        return r.get(SummonerByName(self.Name, key=self.key)).json()

    def __init__(self, SumName, key):
        self.Name = SumName
        self.key = key
        self.raw = self.getRaw()
        self.puu = self.raw.get("puuid")
        self.games = self.getGames()
        self.matches = self.makeMatchList()

    def synergy(self):
        freq = {}
        matchfiles = {"Partners": {}}
        for m in self.matches:
            group = 0
            pnums = self.matches[m].raw.get('info').get('participants')
            for p in pnums:
                tempPU = p.get("puuid")
                if tempPU == self.puu:
                    group = int(p.get('partner_group_id'))
                    for pn in pnums:
                        if pn.get('partner_group_id') == group:
                            p2 = pn.get('puuid')
                            if p2 != self.puu:
                                if (p2 not in matchfiles["Partners"].keys()):
                                    matchfiles["Partners"][p2] = {"Games": [
                                        self.matches[m].raw]}
                                else:
                                    matchfiles["Partners"][p2]["Games"].append(
                                        self.matches[m].raw)
                                if (p2 in freq.keys()):
                                    freq[p2][0] += 1
                                    freq[p2][1] += int(pn.get('placement'))
                                else:
                                    freq[p2] = [1, int(pn.get('placement'))]
                            else:
                                pass
                        else:
                            pass
        for syn in freq:
            freq[syn][1] = round(int(freq[syn][1])/int(freq[syn][0])/2, 3)

        saving = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not saving:
            return
        with open(saving, 'w') as file:
            json.dump(matchfiles, file)

        return freq




        







