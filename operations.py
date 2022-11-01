from ast import operator
from cgi import test
import requests
import json

from codes import clientId, clientSecret, base64Code, redirect_uri, code, refreshToken

testToken="BQDgiQg8FmxzkKc1Vx--phLuwWny8HxZvtuia90iHevxrTEzR24ajnQ0Fyr6qMl2Mw7hiXcy5clw2yBpHUpqsHA3fl8-3i9J-GbgJ-hw08TvCapoBjzpNr45g4jzAx2hgSVkfidQWh03Rwb-iJ81YA"


class Operations:

    def __init__(self):
        self.clientId = clientId
        self.redirect_uri = redirect_uri
        self.accessToken = ""


# log in, get the authorization code from uri
# done manually with this link: 
# https://accounts.spotify.com/authorize?client_id=3d19bbf5a65044c6a9ef4566ad0328c2&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback%2F


# https://accounts.spotify.com/authorize?client_id=3d19bbf5a65044c6a9ef4566ad0328c2&scope=user-read-playback-state&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback%2F


    def requestUserAuthorization(self):

        query = "https://accounts.spotify.com/authorize"

        response = requests.get(query,
                                data={"client_id": clientId,
                                      "response_type": "code",
                                      "redirect_uri": redirect_uri,
                                      "scope": "user-modify-playback-state" + "read-p"
                                      }
        )




# trade auth code for access token and refresh token

    def requestAccessToken(self):

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "authorization_code",
                                       "code": code,
                                       "redirect_uri": redirect_uri},
                                 headers={"Authorization": "Basic M2QxOWJiZjVhNjUwNDRjNmE5ZWY0NTY2YWQwMzI4YzI6ZTUxY2ViZmUxYzAzNDhlMTk3MDg2YzUwNTM2YTNlMDc=",
                                          "Content-Type": "application/x-www-form-urlencoded"})
        response_data = response.json()
        self.accessToken = response_data["access_token"]
        print(response_data)




# use refresh token to get new access token

    def refreshAccessToken(self):
        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refreshToken},
                                 headers={"Authorization": "Basic M2QxOWJiZjVhNjUwNDRjNmE5ZWY0NTY2YWQwMzI4YzI6ZTUxY2ViZmUxYzAzNDhlMTk3MDg2YzUwNTM2YTNlMDc=",
                                          "Content-Type": "application/x-www-form-urlencoded"}
                                       )
        response_data = response.json()
        self.accessToken = response_data["access_token"]



    def playHarry(self):
        query="https://api.spotify.com/v1/me/player/play"

        response = requests.put(query,
                                json={
                                    "context_uri": "spotify:album:5r36AJ6VOJtp00oxSkBZ5h",
                                    "offset": {
                                        "position": 0
                                    },
                                    "position_ms": 0
                                    },
                                headers={"Authorization": f"Bearer {self.accessToken}",
                                         "Content-Type": "application/json"}
                                )
        response_data = response.json()
        print(response_data)




    def getInfo(self):
        
        query = "https://api.spotify.com/v1/me/player/devices"

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"Bearer {self.accessToken}"})
        response_data = response.json()
        print(response_data["devices"])


    def setDevice(self):
        query = "https://api.spotify.com/v1/me/player"
 
        response = requests.get(query,
                                headers={"Authorization": f"Bearer {testToken}",
                                         "Content-Type": "application/json"},
                                json={
                                    "device_ids": [
                                        "af57ea6123bd0b886540046ed12b7a5cb341b229"
                                    ]
                                })
        response_data = response.json()
        print(response_data)