from Consts import MatchByGameID
import requests as r


class match:

    def getMatches(self):  # get Match from gameID
        return r.get(MatchByGameID(self.id, key=self.key)).json()

    def __init__(self, matchID, key):
        self.id = matchID
        self.key = key
        self.raw = self.getMatches()
