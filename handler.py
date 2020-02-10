from utils import *

class Handler:

    def __init__(self, callback):
        self.callback = callback

    def filter(self, update):
        return True

    def call(update):
        if not self.filter(update):
            return

        self.callback(update)

class MessageHandler(Handler):

    def __init__(self, callback):
        super().__init__(callback)

    def filter(self, update):
        if "message" in update:
            return True

        return False

    def call(self, update):
        if not self.filter(update):
            return
        
        self.callback( Message(update['message']) )

class TextMessageHandler(MessageHandler):

    def filter(self, update):
        if not super().filter(update):
            return False

        if not "text" in update['message']:
            return False

        return True