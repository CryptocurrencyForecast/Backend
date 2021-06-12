from psaw import PushshiftAPI
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import json


def get_last_day_post_for_top50():
    binance_url = 'https://api.binance.com/api/v3/exchangeInfo'
    coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': '1',
        'limit': '50'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '914f2649-4495-4906-aadb-e55ea1e56ea2',
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


def get_last_day_post_for_ticker(ticker):
    coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol=' + ticker

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '914f2649-4495-4906-aadb-e55ea1e56ea2',
    }

    session_coinmarketcap = Session()
    session_coinmarketcap.headers.update(headers)

    try:
        response_coinmarketcap = session_coinmarketcap.get(coinmarketcap_url)
        data_coinmarketcap = json.loads(response_coinmarketcap.text)["data"][ticker]
        symbols = {data_coinmarketcap["name"], data_coinmarketcap["symbol"]}
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
            print(post_list)

    return json.dumps(post_list)
