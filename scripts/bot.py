import telebot
from telebot import types

class Bot:
    bot = None
    def __init__(self,token):
        self.bot = telebot.TeleBot(token)
        #main_markup = types.InlineKeyboardMarkup(row_width=2)
        @self.bot.message_handler(commands=["start"])
        def start(message):
            print(message.from_user.id)
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("меню магазина",callback_data='menu')
            button2 = types.InlineKeyboardButton("личный кабинет",callback_data='profile')
            button3 = types.InlineKeyboardButton("faq",callback_data='faq')
            button4 = types.InlineKeyboardButton("отзовы",callback_data='feedback')
            button5 = types.InlineKeyboardButton("гарантии",callback_data='warranty')
            button6 = types.InlineKeyboardButton("подержка",callback_data='support')
            markup.add(button1,button2,button3,button4,button5,button6)
            #main_markup = markup
            self.bot.send_photo(message.chat.id, photo=open("../images/start.jpg","rb"), caption="Привет, вы попали в магазин по продаже свечей!", reply_markup=markup)
        @self.bot.message_handler(commands=["menu"])
        def menu(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("вау",callback_data='menu')
            button2 = types.InlineKeyboardButton("авыаы",callback_data='profile')
            button3 = types.InlineKeyboardButton("авы",callback_data='faq')
            button4 = types.InlineKeyboardButton("отзаовы",callback_data='feedback')
            button5 = types.InlineKeyboardButton("гарантии",callback_data='warranty')
            button6 = types.InlineKeyboardButton("подержка",callback_data='support')
            markup.add(button1,button2,button3,button4,button5,button6)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Меню магазина",message.chat.id,message.message_id,reply_markup=markup)
        def profile(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("история покупок",callback_data='menu')
            button2 = types.InlineKeyboardButton("пополнение",callback_data='profile')
            markup.add(button1,button2)
            self.bot.edit_message_caption("Личный кабинет",message.chat.id,message.message_id,reply_markup=markup)
        def feedback(message):
            self.bot.edit_message_caption("Отзовы",message.chat.id,message.message_id,)
        def FAQ(message):
            self.bot.edit_message_caption("FAQ",message.chat.id,message.message_id)
        def warranty(message):
            self.bot.edit_message_caption("Гарантии",message.chat.id,message.message_id)
        def support(message):
            self.bot.edit_message_caption("Подержка",message.chat.id,message.message_id)
        @self.bot.message_handler(commands=["faq"])
        def faq(message):   
            self.bot.send_message(message.chat.id, "Ответы на часто задаваемые вопросы!")
            
        @self.bot.callback_query_handler(func=lambda callback: True)
        def callback_message(callback):
            if callback.data=='menu':
                menu(callback.message)
                #self.bot.send_message(callback.message.chat.id,"Вы попали в меню")
            elif callback.data=='profile':
                self.bot.send_message(callback.message.chat.id,"Вы попали в профиль")
                profile(callback.message)
            elif callback.data=='faq':
                faq(callback.message)
            elif callback.data=='feedback':
                self.bot.send_message(callback.message.chat.id,"Вы попали в отзовы")
                feedback(callback.message)
            elif callback.data=='warranty':
                self.bot.send_message(callback.message.chat.id,"Вы попали в гарантии")
                warranty(callback.message)
            elif callback.data=='support':
                self.bot.send_message(callback.message.chat.id,"Вы попали в подержку")
                support(callback.message)
    