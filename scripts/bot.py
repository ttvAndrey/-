import telebot
from telebot import types

price_list  = {'estetik 180': 3500,
                'bionika 160': 4200,
                'shick 110': 2600,
                'versal 150': 5000,
                'lounge 50': 450,
                'retro 160': 3600}


class Bot:
    bot = None
    cart = []
    
        
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
            button6 = types.InlineKeyboardButton("коризна",callback_data='cart')
            markup.add(button1,button2,button3,button4,button5,button6)
            #main_markup = markup
            self.bot.send_photo(message.chat.id, photo=open("../images/start.jpg","rb"), caption="Привет, вы попали в магазин по продаже свечей!", reply_markup=markup)
        @self.bot.message_handler()
        def estetik(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='estetik 180')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Estetik Объемом 180 мл, Цена - 3500 ₽",message.chat.id,message.message_id,reply_markup=markup)
        @self.bot.message_handler()
        def bionika(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='bionika 160')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Bionika Объемом 160 мл, Цена - 4200 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def shick(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='shick 110')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Shick Объемом 110 мл, Цена - 2600 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def versal(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='versal 150')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Versal Объемом 150 мл, Цена - 5000 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def lounge(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='lounge 50')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Lounge Объемом 50 мл, Цена - 450 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def retro(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='retro 160')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Retro Объемом 160 мл, Цена - 3600 ₽",message.chat.id,message.message_id,reply_markup=markup)

        @self.bot.message_handler(commands=["menu"])
        def menu(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Коллекция «Estetik” ",callback_data='estetik')
            button2 = types.InlineKeyboardButton("Коллекция «Retro»",callback_data='retro')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Категории",message.chat.id,message.message_id,reply_markup=markup)
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
        def show_cart(message,reciept):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("купить товары в корзине",callback_data='check cart')
            markup.add(button1)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption(reciept,message.chat.id,message.message_id,reply_markup=markup)
        @self.bot.message_handler(commands=["cart"])
        def cart(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("посмотреть корзину",callback_data='show cart')
            markup.add(button1)
            self.bot.edit_message_caption("Личный кабинет",message.chat.id,message.message_id,reply_markup=markup)
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
            elif callback.data=='cart':
                self.bot.send_message(callback.message.chat.id,"Вы попали в корзину")
                cart(callback.message)
            elif callback.data=='show cart':
                self.bot.send_message(callback.message.chat.id,"Вы попали в просмотр корзины")
                show_cart(callback.message,self.check_cart())
            elif callback.data=='estetik':
                self.bot.send_message(callback.message.chat.id,"Вы попали в estetik")
                estetik(callback.message)
            elif callback.data=='estetik':
                self.bot.send_message(callback.message.chat.id,"Вы попали в estetik")
                estetik(callback.message)
            elif callback.data=='bionika':
                self.bot.send_message(callback.message.chat.id,"Вы попали в bionika")
                bionika(callback.message)
            elif callback.data=='shick':
                self.bot.send_message(callback.message.chat.id,"Вы попали в shick")
                shick(callback.message)
            elif callback.data=='versal':
                self.bot.send_message(callback.message.chat.id,"Вы попали в versal")
                versal(callback.message)
            elif callback.data=='lounge':
                self.bot.send_message(callback.message.chat.id,"Вы попали в lounge")
                lounge(callback.message)
            elif callback.data=='retro':
                self.bot.send_message(callback.message.chat.id,"Вы попали в retro")
                retro(callback.message)
            elif callback.data == 'buy cart':
                self.buy()
            else:
                self.cart.append((callback.data,price_list[callback.data]))
            
    def check_cart(self):
        reciept = "Ваш чек:\n"
        for i in range(self.cart):
            reciept+=f"{i+1}. f{self.cart[i][0]} - {self.cart[i][1]}₽"
        return reciept
    def buy_cart(self):
        with open('../orders.txt', 'a', encoding='utf-8') as f:
            data = self.check_cart()
            f.write(data)
        self.cart.clear()