import requests
import json
import time
from utils import *

class Bot:

    def __init__(self, token):
        self.token = token
        self.API_URL = "https://api.telegram.org/bot" + token

        self.limit = 10
        self._lastUpdateId = 0
        self.updateRate = 10

        self.handlers = []

    def start(self):
        while True:
            self.getUpdates()
            time.sleep( 1 / self.updateRate )

    def getMe(self):
        r = requests.get( self.API_URL + "/getMe" )
        data = json.loads(r.content.decode("utf-8"))
        return data['result']

    def getUpdates(self):
        params = {
            'offset': self._lastUpdateId + 1,
            'limit': self.limit
        }

        r = requests.get( self.API_URL + "/getUpdates", params=params )
        data = json.loads(r.content.decode("utf-8"))

        for update in data['result']:

            # Get the highest update id
            if update['update_id'] > self._lastUpdateId:
                self._lastUpdateId = update['update_id']

            print( update )