def SummonerByName(sumName, key, lolRegion='americas'):
    """
    Return: a string of the web qeary to get account info from name
    Args:
        sumName   -- Summoner name (In game name and tagline separated by '/')
        key       -- api key
        lolRegion -- Account region (americas, asia, europe)
    """
    return f'https://{lolRegion}.api.riotgames.com/riot/'\
           f'account/v1/accounts/by-riot-id/{sumName}?api_key={key}'


def GamesByPUU(PUU, key, games=20, tftRegion='americas'):
    """
    Return: a string of the web query to get list of last 20 games
    Args:
        puu       -- Account puuID
        key       -- api key
        games     -- number of games to query
        tftRegion -- Region of TFT server
    """
    return f'https://{tftRegion}.api.riotgames.com/tft/'\
           f'match/v1/matches/by-puuid/{PUU}/'\
           f'ids?start=0&startTime=1710936413&count=30&api_key={key}'


def MatchByGameID(gameID, key, tftRegion='americas'):
    """
    Return: a string of the web query for match data from a game
    Args:
        matchID   -- ID of game
        key       -- api key
        tftRegion -- Region of TFT server
    """
    return f'https://{tftRegion}.api.riotgames.com/tft/'\
           f'match/v1/matches/{gameID}?api_key={key}'


def ProfileBYpuu(puu, key, tftRegion='americas'):
    """
    Return: a string of the web query for account info from puuid
    Args:
        puu       -- Account puuID
        key       -- api key
        tftRegion -- Region of TFT server
    """
    return f'https://{tftRegion}.api.riotgames.com/riot/'\
           f'account/v1/accounts/by-puuid/{puu}?api_key={key}'
