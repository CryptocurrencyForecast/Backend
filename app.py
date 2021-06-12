from flask import Flask, make_response
from reddit import get_last_day_post_for_ticker

app = Flask(__name__)

@app.route('/last-post/<ticker>', methods=['GET'])
def get_posts_for_ticker(ticker):
    data = get_last_day_post_for_ticker(ticker)
    r = make_response(data)
    r.mimetype = 'application/json'
    return r
