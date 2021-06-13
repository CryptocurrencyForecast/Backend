import json
from datetime import datetime

from psaw import PushshiftAPI
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def get_trending_on_reddit():
    nomics_url = 'https://api.nomics.com/v1/currencies/ticker?key=f40c6b7456c197028c38acdd0a2b6c23&status=active&interval=1d&per-page=8&page=1&sort=rank'
    session_nomics = Session()

    symbols = []

    try:
        response_nomics = session_nomics.get(nomics_url)
        data_nomics = json.loads(response_nomics.text)
        for crypto in data_nomics:
            symbols.append([crypto["symbol"], crypto["name"], 0])
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
        for word in words:
            for symbol in symbols:
                if word in symbol:
                    symbol[2] += 1

    return json.dumps(symbols)


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
