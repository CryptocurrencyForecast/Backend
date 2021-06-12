from psaw import PushshiftAPI
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import datetime
import json

binance_url = 'https://api.binance.com/api/v3/exchangeInfo'
coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '2000'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '673ba535-54db-4d06-8cba-26e27637ef95',
}

session_binance = Session()
session_coinmarketcap = Session()
session_coinmarketcap.headers.update(headers)

try:
    response_binance = session_binance.get(binance_url)
    response_coinmarketcap = session_coinmarketcap.get(coinmarketcap_url, params=parameters)
    data_binance = json.loads(response_binance.text)
    data_coinmarketcap = json.loads(response_coinmarketcap.text)
    symbols = {}
    symbols_coinmarketcap = {}
    symbols_binance = list(set([cryto['baseAsset'] for cryto in data_binance['symbols']]))
    for crypto in data_coinmarketcap['data']:
        symbols_coinmarketcap[crypto['symbol']] = crypto['name']
    for symbol in symbols_coinmarketcap:
        if symbol in symbols_binance:
            symbols[symbol] = symbols_coinmarketcap[symbol]
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

api = PushshiftAPI()

start_time = int(datetime.datetime(2021, 1, 3).timestamp())

submissions = api.search_submissions(after=start_time,
                                     subreddit='CryptoCurrency',
                                     filter=['url', 'author', 'title', 'subreddit'])
print('')
for submission in submissions:
    words = submission.title.split()
    crytotag = {}
    for word in words:
        if word in symbols:
            crytotag[word] = symbols[word]
        elif word in symbols.values():
            crytotag[list(symbols.keys())[list(symbols.values()).index(word)]] = word

    if len(crytotag):
        print(crytotag)
        print(submission.title)
        print(submission.url)
