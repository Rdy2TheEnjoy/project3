import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.apilayer.com/exchangerates_data/latest"

def get_exchange_rate(currency_code):
    headers = {'apikey' : API_KEY}
    params = {'symbols' : 'RUB'}

    if currency_code != 'EUR':
        params['symbols'] +=  f',{currency_code}'

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)

    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json()
    rates = data.get('rates', {})

    if currency_code == 'RUB':
        return 1.0

    if currency_code == 'EUR':
        return rates.get("RUB")

    eur_to_rub = rates.get('RUB')
    eur_to_currency = rates.get(currency_code)

    if not eur_to_run or eur_to_currency:
        return eur_to_rub / eur_to_currency

def convert_to_rubles(transactions):
    amount = transactions.get('amount')
    currency = transactions.get('currency', 'RUB')
    if currency == 'RUB':
        return float(amount)

    rate = get_exchange_rate(currency)
    if rate is None:
        return None

    return round(float(amount) * rate, 2)

