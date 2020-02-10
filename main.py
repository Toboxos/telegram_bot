from bot import Bot
from utils import *
from handler import *

TOKEN = open(".token", "r").read()

bot = Bot(TOKEN)

def messageReceived(message):
    user = message.fromUser
    text = message.text.lower()

    if any(x in text for x in ['zeig', 'coole', 'website']):
        message.reply("https://www.toboxos.de", bot)
        return

    message.chat.sendText( "Hallo " + user.first_name, bot)

bot.addHandler( TextMessageHandler(messageReceived) )
bot.start()