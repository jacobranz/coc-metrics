from api.test_api import Clan
from api.test_api import Player
from data.buildData import playerData
import json

#API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNjNmRlMjUzLWE2ZGUtNDg0Ni1iM2U1LWY1ZjUyMjY5ZWQzMyIsImlhdCI6MTc4ODQ5NTAzNywic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc2LjgzLjExMC4yMzQiXSwidHlwZSI6ImNsaWVudCJ9XX0.N3tQyGxUCACOYHzGmd12Af6kmVSfcuY3ssjLLfUSFUdK_rEnbQSsT0yqRHNSxIgIlwrfOdAbjT4WT9OnJJvAEA"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjcyYTI2NmE2LTg1MDctNGQ3OS05NjVkLTM5MzA4OWU4Mzc4OCIsImlhdCI6MTc4NTEwODE1Mywic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ3LjE1MC4xNzEuMjIyIl0sInR5cGUiOiJjbGllbnQifV19.GFtnAg3097GwaHZSzNFJrgzNjdfKgzyRfYVWUsg-ZSiD_ykf1-oMrjkMNZIvgyHA3rOBA1p9wzLWHyPP4DpUyw"

playerTags = [
    "#9209UQ02V"
]
fields = [
    "name", 
    "tag", 
    "role", 
    "expLevel", 
    "trophies", 
    "warStars",
    "donations"
]
clanTags = [
    "#2Q2YL8VGO",
    #"#2Q2YL8VGO/warlog",
    #"#2Q2YL8VGO/currentwar/leaguegroup"
    #"#2Q2YL8VGO/currentwar"
    #"#2Q2YL8VGO/members",
    #"#2Q2YL8VGO/capitalraidseasons"
]
clanFields = [
    "name",
    "memberList"
]

def getClanData():
    for tag in clanTags:
        clan = Clan(API_TOKEN, tag)
        return clan.get_info()

def getPlayerData():
    for tag in playerTags:
        player = Player(API_TOKEN, tag)
        return player.get_info()

with open("data.json", "w") as f:
    print(getClanData(), file=f)
