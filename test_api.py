import requests
import json
import csv

class Player():
    def __init__(self, token, tag):
        self.apiToken = token
        self.playerTag = tag

    def get_info(self):
        encoded_tag = self.playerTag.replace("#", "%23")
        url = f"https://api.clashofclans.com/v1/players/{encoded_tag}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.apiToken}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    def queryPlayer(self, fields):
        self.playerInfo = self.get_info()

        return {
            field: self.playerInfo[field]
            for field in fields
            if field in self.playerInfo
        }

class Clan():
    def __init__(self, token, tag):
        self.apiToken = token
        self.clanTag = tag

    def get_info(self):
        encoded_tag = self.clanTag.replace("#", "%23")
        url = f"https://api.clashofclans.com/v1/clans/{encoded_tag}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.apiToken}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()
    
    def queryClan(self):
        self.clanInfo = self.get_info()

        return {
            field: self.clanInfo[field]
            for field in fields
            if field in self.clanInfo
        }
    
    def getMemberList(self):
        self.members = self.get_info()
        
        #for member in self.members['memberList']:
        #    print(member['tag'])

    def createMemberList(self):
        self.memberList = []
        self.members = self.get_info()

        for memberTag in self.members['memberList']:
            self.memberList.append(memberTag['tag'])
        
        return self.memberList

# Instantiate class
#API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjMzFhYTEwLTRkYTYtNGJmMi05NjkyLTViODM4ODg3YmNhYyIsImlhdCI6MTc4NjQxODIyMiwic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4Ny4xMy4xNDMuMjA0Il0sInR5cGUiOiJjbGllbnQifV19._tOYShTW-u0DO58wfHpqPFKMjzqV6xkwZ1mwse4lfd2qmH8LOKLKZb21Q78xOuMTZ0CiVX6iPi3x0xeph1vOdQ"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImVlYmUwNDE2LTE2NjktNDhkYi1iMmUzLTYwY2ZjNmU5ZGJiYiIsImlhdCI6MTc4Njc1NDY5MSwic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk4Ljk3LjI2LjE5Il0sInR5cGUiOiJjbGllbnQifV19.LdR9zufFXORWF-V6QGVAsfoQEyNNWXiwyJK-0Jvxe-QHIai5_17mi0XtY--MrnS_-1jPKTmwc9wP5KHwHyebzg"

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
    "#2Q2YL8VGO"
]
clanFields = [
    "name",
    "memberList"
]

'''
with open("coc_clan_data.csv", "a", newline="") as clanscv:
    writer = csv.DictWriter(clanscv, fieldnames=clanFields)
    writer.writeheader()

    for tag in clanTags:
        clan = Clan(API_TOKEN, tag)

        data = clan.queryClan(clanFields)

        writer.writerow(data)
'''
for tag in clanTags:
    clan = Clan(API_TOKEN, tag)
    clan.get_info()
    clan.getMemberList()

with open("coc_clan_data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for tag in clan.createMemberList():
        player = Player(API_TOKEN, tag)

        data = player.queryPlayer(fields)

        writer.writerow(data)