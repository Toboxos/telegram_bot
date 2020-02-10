import requests
import json
import time
from utils import *

class Bot:

    def __init__(self, token):
        self.token = token
        self.API_URL = "https://api.telegram.org/bot" + token
        self.FILE_URL = "https://api.telegram.org/file/bot" + token

        self.limit = 10
        self._lastUpdateId = 0
        self.updateRate = 0.5

        self.handlers = []

    def start(self):
        while True:
            self.getUpdates()
            time.sleep( 1 / self.updateRate )

    def getMe(self):
        r = requests.get( self.API_URL + "/getMe" )
        data = json.loads(r.content.decode("utf-8"))
        return User(data['result'])

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

            for handler in self.handlers:
                handler.call( update )

    def sendMessage(self, chat_id, text, **kwargs):
        params = {
            'chat_id': chat_id,
            'text': text
        }
        params.update( kwargs )

        r = requests.post( self.API_URL + "/sendMessage", params=params)
        data = json.loads(r.content.decode("utf-8"))

        if data['ok'] != True:
            return False

        return Message(data['result'])

    def downloadFile(self, file_id):
        r = requests.get( self.API_URL + "/getFile", params={'file_id': file_id})
        data = json.loads( r.content.decode("utf-8") )

        if data['ok'] != True:
            return False

        r = requests.get( self.FILE_URL + "/" + data['result']['file_path'] )
        return r.content

    def sendDocument(self, chat_id, name, file, **kwargs):
        params = {'chat_id': chat_id,}
        params.update(kwargs)

        r = requests.request( "get", self.API_URL + "/sendDocument", params=params )
        r = requests.post( r.url, files={'document': (name, file)} )

        data = json.loads(r.content.decode("utf-8"))
        return Message( data['result'] ) 
 
    def addHandler(self, handler):
        self.handlers.append( handler )