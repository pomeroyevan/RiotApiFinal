region_tft = 'americas'
region_league = 'na1'
summoner_name = 'thenucleartoast'


def SummonerByName(sumName, key, lolRegion='americas'):
    return f'https://{lolRegion}.api.riotgames.com/riot/
    account/v1/accounts/by-riot-id/{sumName}?api_key={key}'


def GamesByPUU(PUU, key, matches=20, tftRegion='americas'):
    return f'https://{tftRegion}.api.riotgames.com/tft/
    match/v1/matches/by-puuid/{PUU}/ids?start=0&startTime=1710936413&count=30&api_key={key}'


def MatchByGameID(matchID, key, tftRegion='americas'):
    return f'https://{tftRegion}.api.riotgames.com/tft/
    match/v1/matches/{matchID}?api_key={key}'


def ProfileBYpuu(puu, key, tftRegion='americas'):
    return f'https://{tftRegion}.api.riotgames.com/riot/
    account/v1/accounts/by-puuid/{puu}?api_key={key}'
