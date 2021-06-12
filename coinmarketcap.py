from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '673ba535-54db-4d06-8cba-26e27637ef95',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    symbols = {}
    for crypto in data['data']:
        symbols[crypto['symbol']] = crypto['name']
    print(data)
    symbols = [cryto['symbol'] for cryto in data['data']]
    print(symbols)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
