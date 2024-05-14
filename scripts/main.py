import telebot

token = "7163183430:AAGfe5OsU3xeyvKfisCATViFYKzAVZXjAEA"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет,вы попали в магазин свеч!")

bot.polling(none_stop=True)
