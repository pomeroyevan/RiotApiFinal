from Constants import MatchByGameID
import requests as r


class match:
    """All data for one tft Game"""
    def getMatches(self):
        """get match from gameID"""
        return r.get(MatchByGameID(self.id, key=self.key)).json()

    def __init__(self, matchID, key):
        # gameID for match data
        self.id = matchID
        # api key
        self.key = key
        # get match data
        self.raw = self.getMatches()
