import json
import requests
from config import keys
from secret import apikey



class ConversionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):
        if base == quote:
            raise ConversionException(f'Одинаковые валюты нельзя посчитать')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось найти валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось найти валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        url = f'https://api.apilayer.com/fixer/convert?to={base_ticker}&from={quote_ticker}&amount={amount}'

        payload = {}

        headers = {
            "apikey": apikey
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        respon222 = response.json()

        result = (respon222['result'])

        return result


