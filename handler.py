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

class DocumentHandler(MessageHandler):

    def __init__(self, callback, filterOptions={}):
        self.callback = callback
        self.filterOptions = filterOptions

    def filter(self, update):
        if not super().filter(update):
            return False

        if not "document" in update['message']:
            return False

        doc = Document(update['message']['document'])
        if "file_size" in self.filterOptions and doc.file_size > self.filterOptions['file_size']:
            return False

        if "mime_type" in self.filterOptions and doc.mime_type != self.filterOptions['mime_type']:
            return False

        if "file_name" in self.filterOptions and doc.file_name != self.filterOptions['file_name']:
            return False

        return True