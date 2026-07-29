import requests
import json

class playerInfo():
    def __init__(self, token, tag):
        self.apiToken = token
        self.playerTag = tag
        # Define configuration variables
        apiToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjcyYTI2NmE2LTg1MDctNGQ3OS05NjVkLTM5MzA4OWU4Mzc4OCIsImlhdCI6MTc4NTEwODE1Mywic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ3LjE1MC4xNzEuMjIyIl0sInR5cGUiOiJjbGllbnQifV19.GFtnAg3097GwaHZSzNFJrgzNjdfKgzyRfYVWUsg-ZSiD_ykf1-oMrjkMNZIvgyHA3rOBA1p9wzLWHyPP4DpUyw"
        playerTag = "#9209UQO2V"  # Replace with your actual clan tag

        # URL-encode the '#' character for the endpoint
        encoded_tag = playerTag.replace("#", "%23")
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

    def getPlayerName(self):
        try:
            self.playerName = self.data['name']
        except:
            print("Something went wrong when trying to get player name!")

        print(self.playerName)

player = playerInfo("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjcyYTI2NmE2LTg1MDctNGQ3OS05NjVkLTM5MzA4OWU4Mzc4OCIsImlhdCI6MTc4NTEwODE1Mywic3ViIjoiZGV2ZWxvcGVyL2ZlMzA3MDZmLWJkNjgtNGFjOC04ZGQ1LTFkMDVjZTBhNTFmMyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ3LjE1MC4xNzEuMjIyIl0sInR5cGUiOiJjbGllbnQifV19.GFtnAg3097GwaHZSzNFJrgzNjdfKgzyRfYVWUsg-ZSiD_ykf1-oMrjkMNZIvgyHA3rOBA1p9wzLWHyPP4DpUyw", 
    "#2Q2YL8VGO"
    )
player.getPlayerName()