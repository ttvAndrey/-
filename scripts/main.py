import telebot
from bot import Bot
token = open("../token.pem","r").readline()
bot = Bot(token).bot
bot.polling(none_stop=True)
