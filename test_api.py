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

# Instantiate class
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjMzFhYTEwLTRkYTYtNGJmMi05NjkyLTViODM4ODg3YmNhYyIsImlhdCI6MTc4NjQxODIyMiwic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4Ny4xMy4xNDMuMjA0Il0sInR5cGUiOiJjbGllbnQifV19._tOYShTW-u0DO58wfHpqPFKMjzqV6xkwZ1mwse4lfd2qmH8LOKLKZb21Q78xOuMTZ0CiVX6iPi3x0xeph1vOdQ"

playerTags = [
    "#GOY9G8UOQ",
    "#GQ2U8C22U"
]
fields = [
    "name", 
    "tag", 
    "role", 
    "expLevel", 
    "trophies", 
    "warStars"
]

with open("coc_clan_data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for tag in playerTags:
        player = Player(API_TOKEN, tag)

        data = player.queryPlayer(fields)

        writer.writerow(data)