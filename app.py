from flask import Flask, make_response
from binance_api import get_account_balance
from reddit import get_last_day_post_for_ticker, get_trending_on_reddit
from nomics import get_information_nomics
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/last-posts/<ticker>', methods=['GET'])
def get_last_posts_for_ticker(ticker):
    data = get_last_day_post_for_ticker(ticker)
    r = make_response(data)
    r.mimetype = 'application/json'
    return r


@app.route('/balance/<token>', methods=['GET'])
def get_balance(token):
    data = get_account_balance(token)
    r = make_response(data)
    r.mimetype = 'application/json'
    return r


@app.route('/trending-currencies', methods=['GET'])
def get_trending_currencies():
    data = get_trending_on_reddit()
    r = make_response(data)
    r.mimetype = 'application/json'
    return r


@app.route('/nomics/<token>', methods=['GET'])
def get_information_crypto(token):
    data = get_information_nomics(token)
    r = make_response(data)
    r.mimetype = 'application/json'
    return r
