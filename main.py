from bot import Bot
from utils import *
from handler import *
import json
import io

TOKEN = open(".token", "r").read()

bot = Bot(TOKEN)

def messageReceived(message):
    user = message.fromUser
    text = message.text.lower()

    if any(x in text for x in ['zeig', 'coole', 'website']):
        message.reply("https://www.toboxos.de", bot)
        return

    message.chat.sendText( "Hallo " + user.first_name, bot)

def docRecevied(message):
    user = message.fromUser
    message.chat.sendText("Danke " + user.first_name, bot)

    doc = message.document
    if doc.mime_type == "application/json":
        content = doc.download(bot).decode("utf-8")

        try:
            data = json.loads(content)
            data['answer'] = "answer"
            content = json.dumps(data)
        except Exception as e:
            print(e)

        message.chat.sendDocument( "Aswer.json", io.StringIO(content), bot )

bot.addHandler( TextMessageHandler(messageReceived) )
bot.addHandler( DocumentHandler(docRecevied) )
bot.start()