import telebot
import requests
import json

currency = {'доллар': 'USD',
            'евро': 'EUR',
            'рубль': 'RUB'}

TOKEN = "5294894728:AAEQ4nEAkrt7yyygr6Yvc7ZZ26Bvm-Cxl2Q"

bot = telebot.TeleBot('5294894728:AAEQ4nEAkrt7yyygr6Yvc7ZZ26Bvm-Cxl2Q')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 f"<Введите имя валюты, цену которой вы хотите узнать>\
<имя валюты, в которой надо узнать цену первой валюты>\
 <количество первой валюты>. Чтобы увидеть весь список доступных валют, введите /currency")
    print(message.text)


@bot.message_handler(commands=['currency'])
def Currency(message: telebot.types.Message):
    text = 'Вам доступны следующие валюты:'
    for key in currency.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_type =['text', ])
def converter(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://free.currconv.com/api/v7/convert?apiKey=cd2ff852330c08894153&q={currency[quote]}_{currency[base]}&compact=ultra')
    total_base = json.loads(r.content)[currency[base]]
    text = f'За {amount} {quote} сейчас дают - {total_base}'
    bot.send_message(message.chat.id, text)



bot.polling()