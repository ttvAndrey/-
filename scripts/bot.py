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
            button4 = types.InlineKeyboardButton("отзывы",callback_data='feedback')
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
            button2 = types.InlineKeyboardButton("Вернуться к коллекциям",callback_data='menu')#здесь 1
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/estetick.png",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Estetik Объемом 180 мл, Цена - 3500 ₽",message.chat.id,message.message_id,reply_markup=markup)
        @self.bot.message_handler()
        def bionika(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='bionika 160')
            button2 = types.InlineKeyboardButton("Вернуться к коллекциям",callback_data='menu')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/bionika.png",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Bionika Объемом 160 мл, Цена - 4200 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def shick(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='shick 110')
            button2 = types.InlineKeyboardButton("Вернуться к коллекциям",callback_data='menu')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/shik.png",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Shick Объемом 110 мл, Цена - 2600 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def versal(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='versal 150')
            button2 = types.InlineKeyboardButton("Вернуться к коллекциям",callback_data='menu')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/versal.png",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Versal Объемом 150 мл, Цена - 5000 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def lounge(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='lounge 50')
            button2 = types.InlineKeyboardButton("Вернуться к коллекциям",callback_data='menu')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/lounge.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Lounge Объемом 50 мл, Цена - 450 ₽",message.chat.id,message.message_id,reply_markup=markup)
        def retro(message):#здесь
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Купить",callback_data='retro 160')
            button2 = types.InlineKeyboardButton("Вернуться к коллекциям",callback_data='menu')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/retro.png",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Купить Retro Объемом 160 мл, Цена - 3600 ₽",message.chat.id,message.message_id,reply_markup=markup)

        @self.bot.message_handler(commands=["menu"])
        def menu(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Коллекция «Estetik” ",callback_data='estetik')
            button2 = types.InlineKeyboardButton("Коллекция «Retro»",callback_data='retro')
            button3 = types.InlineKeyboardButton("Коллекция «Lounge»",callback_data='lounge')
            button4 = types.InlineKeyboardButton("Коллекция «Versal»",callback_data='versal')
            button5 = types.InlineKeyboardButton("Коллекция «Shick»",callback_data='shick')
            button6 = types.InlineKeyboardButton("Коллекция «Bionika»",callback_data='bionika')
            button6 = types.InlineKeyboardButton("Коллекция «Bionika»",callback_data='bionika')
            button7 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1,button2,button3,button4,button5,button6,button7)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption("Категории",message.chat.id,message.message_id,reply_markup=markup)
        def profile(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("история покупок",callback_data='cart')
            button2 = types.InlineKeyboardButton("пополнение",callback_data='profile')
            button3 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1,button2,button3)
            self.bot.edit_message_caption("Личный кабинет",message.chat.id,message.message_id,reply_markup=markup)
        def feedback(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1)
            self.bot.edit_message_caption("отзывы находятся по ссылке:https://t.me/+sV3jqC7YqA9hZGUy",message.chat.id,message.message_id,reply_markup=markup)


        def FAQ(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1)
            self.bot.edit_message_caption("FAQ",message.chat.id,message.message_id,reply_markup=markup)
        def warranty(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1)
            self.bot.edit_message_caption("Гарантии https://telegra.ph/Otvety-na-CHasto-zadavaemye-voprosy-06-02-6",message.chat.id,message.message_id,reply_markup=markup)
        def support(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1)
            self.bot.edit_message_caption("Подержка",message.chat.id,message.message_id,reply_markup=markup)
        @self.bot.message_handler(commands=["faq"])
        def faq(message):   
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1)
            self.bot.edit_message_caption("Ответы на часто задаваемые вопросы! https://telegra.ph/Otvety-na-CHasto-zadavaemye-voprosy-06-02-6",message.chat.id,message.message_id,reply_markup=markup)

            #self.bot.send_message(message.chat.id, "Ответы на часто задаваемые вопросы! https://telegra.ph/Otvety-na-CHasto-zadavaemye-voprosy-06-02-6",reply_markup=markup)
        def show_cart(message,reciept):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("купить товары в корзине",callback_data='buy cart')
            button2 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1,button2)
            self.bot.edit_message_media(media=types.InputMediaPhoto(open("../images/menu.jpg",'rb')),chat_id=message.chat.id,message_id=message.message_id)
            self.bot.edit_message_caption(reciept,message.chat.id,message.message_id,reply_markup=markup)
        @self.bot.message_handler(commands=["cart"])
        def cart(message):
            markup = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("посмотреть корзину",callback_data='show cart')
            button2 = types.InlineKeyboardButton("Вернуться к меню",callback_data='start')
            markup.add(button1,button2)
            self.bot.edit_message_caption("Личный кабинет",message.chat.id,message.message_id,reply_markup=markup)
        @self.bot.callback_query_handler(func=lambda callback: True)
        def callback_message(callback):
            if callback.data=='start':
                start(callback.message)
            elif callback.data=='menu':
                menu(callback.message)
                #self.bot.send_message(callback.message.chat.id,"Вы попали в меню")
            elif callback.data=='profile':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в профиль")
                profile(callback.message)
            elif callback.data=='faq':
                faq(callback.message)
            elif callback.data=='feedback':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в отзывы")
                feedback(callback.message)
            elif callback.data=='warranty':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в гарантии")
                warranty(callback.message)
            elif callback.data=='support':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в подержку")
                support(callback.message)
            elif callback.data=='cart':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в корзину")
                cart(callback.message)
            elif callback.data=='show cart':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в просмотр корзины")
                show_cart(callback.message,self.check_cart())
            elif callback.data=='estetik':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в estetik")
                estetik(callback.message)
            elif callback.data=='bionika':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в bionika")
                bionika(callback.message)
            elif callback.data=='shick':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в shick")
                shick(callback.message)
            elif callback.data=='versal':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в versal")
                versal(callback.message)
            elif callback.data=='lounge':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в lounge")
                lounge(callback.message)
            elif callback.data=='retro':
                #self.bot.send_message(callback.message.chat.id,"Вы попали в retro")
                retro(callback.message)
            elif callback.data == 'buy cart':
                self.buy_cart()
            else:
                self.cart.append((callback.data,price_list[callback.data]))
            
    def check_cart(self):
        reciept = "Ваш чек:\n"
        for i in range(len(self.cart)):
            reciept+=f"{i+1}. {self.cart[i][0]} - {self.cart[i][1]}₽\n"
        return reciept
    def buy_cart(self):
        with open('../orders.txt', 'a', encoding='utf-8') as f:
            data = self.check_cart().split('\n')
            for el in data:
                f.write(el+'\n')
        self.cart.clear()