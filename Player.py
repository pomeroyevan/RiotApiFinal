import requests as r
from Constants import SummonerByName, GamesByPUU
from Match import match
import json
from tkinter import filedialog


class player:
    """Data of one player's account and all matches"""
    def getGames(self):
        """Get all gameIDs for the player"""
        games = r.get(GamesByPUU(self.puu, key=self.key)).json()
        return games

    def makeMatchList(self):
        """Make a list of all the matches for the player"""
        matches = {}
        for game in self.games:
            newm = match(game, key=self.key)
            if f"{newm.raw.get('info').get('tft_game_type')}" == 'pairs':
                matches.update({game: newm})
                # creates match objects from gameIDs in dictionary
        return matches

    def getRaw(self):
        """Get json account data from summoner name"""
        return r.get(SummonerByName(self.Name, key=self.key)).json()

    def __init__(self, SumName, key):
        # summoner name
        self.Name = SumName
        # api key
        self.key = key
        # account data
        self.raw = self.getRaw()
        # account puuID
        self.puu = self.raw.get("puuid")
        # list of past gameIDs
        self.games = self.getGames()
        # list of past matches
        self.matches = self.makeMatchList()

    def synergy(self):
        """
        Returns: String of Partner Synergy summary statistics
        Function: Saves json file of matches by partner
        """
        # summary stats for synergy
        freq = {}
        # matches by parrtner player
        matchfiles = {"Partners": {}}
        for m in self.matches:
            group = 0
            pnums = self.matches[m].raw.get('info').get('participants')
            for p in pnums:
                tempPU = p.get("puuid")
                # find team queried player is on
                if tempPU == self.puu:
                    group = int(p.get('partner_group_id'))
                    for pn in pnums:
                        # check if player is teammate
                        if pn.get('partner_group_id') == group:
                            p2 = pn.get('puuid')
                            if p2 != self.puu:
                                # add to match list
                                if (p2 not in matchfiles["Partners"].keys()):
                                    matchfiles["Partners"][p2] = {"Games": [
                                        self.matches[m].raw]}
                                else:
                                    matchfiles["Partners"][p2]["Games"].append(
                                        self.matches[m].raw)
                                # add to summary stats
                                if (p2 in freq.keys()):
                                    freq[p2][0] += 1
                                    freq[p2][1] += int(pn.get('placement'))
                                else:
                                    freq[p2] = [1, int(pn.get('placement'))]
        # calculate summary stats
        for syn in freq:
            freq[syn][1] = round(int(freq[syn][1])/int(freq[syn][0])/2, 3)
        # save file request
        saving = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not saving:
            return
        # save match data to file
        with open(saving, 'w') as file:
            json.dump(matchfiles, file)
        return freq
