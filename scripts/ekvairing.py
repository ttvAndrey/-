import uuid

from yookassa import Configuration, Payment

Configuration.account_id = "Candless"
Configuration.secret_key = "777"
reciept = "Заказы: estetik 50 - 3500, estetik 70 - 4000"
full_price = 7500
payment = Payment.create({
    "amount": {
        "value": f"{full_price}.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://t.me/CandlessaleBot"
    },
    "capture": True,
    "description": "Заказ №1"
}, uuid.uuid4())


# ссылка - для работы с юкассой - https://yookassa.ru/developers/payment-acceptance/getting-started/quick-start?codeLang=python