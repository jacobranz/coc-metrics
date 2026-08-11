import requests
import json
import csv

class player():
    def __init__(self, token, tag):
        self.apiToken = token
        self.playerTag = tag
        # Define configuration variables
        #apiToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhkY2IyMjcxLTFlNzQtNGFjYi1iNWMwLTI3OWYxNDNjMjhjNSIsImlhdCI6MTc4NTI5ODgwMywic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc2LjMzLjc2LjgxIl0sInR5cGUiOiJjbGllbnQifV19.sgfyaaIhbQOBMrvhVpM2_Wt9PADL56T7TfPS3tq3kiPEFExXwb-s9px6DT4ob2H8T3QlnNgk2CcbWGIFvaBO7A"
        #playerTag = "#9209UQO2V"  # Replace with your actual clan tag

        # URL-encode the '#' character for the endpoint
        encoded_tag = self.playerTag.replace("#", "%23")
        self.url = f"https://api.clashofclans.com/v1/players/{encoded_tag}"

        # Set up the authorization headers
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.apiToken}"
        }

        self.response = requests.get(self.url, headers=self.headers)
        self.data = self.response.json()

    def _getPlayerInfo(self):
        return self.data

    def getPlayerInfo(self):
        print(type(self._getPlayerInfo()))

    def queryPlayer(self, keyList, playerDict):
        self.keyList = keyList
        self.playerDict = playerDict
        self.data = {}
        for key in self.keyList:
            self.data[key] = self.playerDict[key]
        return self.data

# Instantiate class
player = player("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhjMzFhYTEwLTRkYTYtNGJmMi05NjkyLTViODM4ODg3YmNhYyIsImlhdCI6MTc4NjQxODIyMiwic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4Ny4xMy4xNDMuMjA0Il0sInR5cGUiOiJjbGllbnQifV19._tOYShTW-u0DO58wfHpqPFKMjzqV6xkwZ1mwse4lfd2qmH8LOKLKZb21Q78xOuMTZ0CiVX6iPi3x0xeph1vOdQ", 
    "#9209UQO2V"
    )
queryList = ["name", "tag", "role", "expLevel", "trophies", "warStars"]
playerInfo = player._getPlayerInfo()
data = player.queryPlayer(queryList, playerInfo)
with open('coc_clan_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=playerInfo)
    writer.writerows(data)