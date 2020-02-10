from bot import Bot

TOKEN = open(".token", "r").read()

bot = Bot(TOKEN)
bot.start()