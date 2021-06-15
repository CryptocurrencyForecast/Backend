import requests
import json


def get_marketcap_information_ticker(ticker):
    coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol=' + ticker

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '914f2649-4495-4906-aadb-e55ea1e56ea2',
    }

    data = requests.get(url=coinmarketcap_url, headers=headers).json()
    return json.dumps(data)
