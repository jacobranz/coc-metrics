import matplotlib as plt
import numpy as np

class playerData():
    # Graph player data
    def graphPlayer(data):
        player = np.array(data)
        return player

class war():
    def __init__(self, data):
        self.data = data

    def parseWar(self):
        return {
            "result": self.data["result"],
            "endTime": self.data["endTime"],
            "teamSize": self.data["teamSize"],
            "clanTag": self.data["clan"]["tag"],
            "clanName": self.data["clan"]["name"],
            "clanLevel": self.data["clan"]["clanLevel"],
            "clanAttacks": self.data["clan"]["attacks"],
            "clanStars": self.data["clan"]["stars"],
            "clanDestrPer": self.data["clan"]["destructionPercentage"],
            "clanExpEarn": self.data["clan"]["expEarned"],
            "oppTag": self.data["opponent"]["tag"],
            "oppName": self.data["opponent"]["name"],
            "oppLevel": self.data["opponent"]["clanLevel"],
            "oppStars": self.data["opponent"]["stars"],
            "oppDestrPer": self.data["opponent"]["destructionPercentage"]
        }

    def getMembers(self):
        pass

    def getAttacks(self):
        pass