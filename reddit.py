from psaw import PushshiftAPI
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import json

""""
def get_last_day_post_for_top50():
    binance_url = 'https://api.binance.com/api/v3/exchangeInfo'
    coin_guecko_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'

    session_binance = Session()
    session_coinguecko = Session()

    try:
        response_binance = session_binance.get(binance_url)
        response_coinguecko = session_coinguecko.get(coin_guecko_url)
        data_binance = json.loads(response_binance.text)
        data_coinmarketcap = json.loads(response_coinguecko.text)
        symbols = {}
        symbols_coinmarketcap = {}
        symbols_binance = list(set([cryto['baseAsset'] for cryto in data_binance['symbols']]))
        for crypto in data_coinmarketcap:
            symbols_coinmarketcap[crypto['symbol']] = crypto['name']
        for symbol in symbols_coinmarketcap:
            if symbol in symbols_binance:
                symbols[symbol] = symbols_coinmarketcap[symbol]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    api = PushshiftAPI()

    start_time = int(datetime(2021, 6, 4).timestamp())
    end_time = int(datetime(2021, 6, 5).timestamp())

    submissions = api.search_submissions(after=start_time,
                                         before=end_time,
                                         subreddit='CryptoCurrency',
                                         filter=['url', 'author', 'title', 'subreddit'])
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
            
"""


def get_last_day_post_for_ticker(ticker):
    nomics_url = "https://api.nomics.com/v1/currencies?key=f40c6b7456c197028c38acdd0a2b6c23&ids=" + ticker + "&attributes=id,name"

    session_nomics = Session()

    try:
        response_nomics = session_nomics.get(nomics_url)
        data_nomics = json.loads(response_nomics.text)[0]
        symbols = {data_nomics["name"], data_nomics["id"]}
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    api = PushshiftAPI()

    start_time = int(datetime(2021, 6, 4).timestamp())
    end_time = int(datetime(2021, 6, 5).timestamp())

    submissions = api.search_submissions(after=start_time,
                                         before=end_time,
                                         subreddit='CryptoCurrency',
                                         filter=['url', 'author', 'title', 'subreddit'])
    post_list = []
    for submission in submissions:
        words = submission.title.split()
        total = 0
        for word in words:
            if word in symbols:
                total += 1
        if total != 0:
            item = {"ticker": ticker, "title": submission.title, "url": submission.url}
            post_list.append(item)
        if len(post_list) == 10:
            break

    return json.dumps(post_list)
