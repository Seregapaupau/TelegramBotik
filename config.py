import requests
import json

currency = {'доллар': 'USD',
            'евро': 'EUR',
            'рубль': 'RUB'}

quote ='евро'
base = 'рубль'

r = requests.get(f'https://free.currconv.com/api/v7/convert?apiKey=cd2ff852330c08894153&q={currency[quote]}_{currency[base]}&compact=ultra')
text = json.loads(r.content)[currency[base]]
print(text)