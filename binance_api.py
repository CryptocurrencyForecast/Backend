from binance.client import Client
import json


def get_account_balance(token):
    # TESTNET CONFIG
    api_key = token[:64]
    api_secret = token[64:]
    client = Client(api_key, api_secret, testnet=True)

    # Loading balances
    balance = client.get_account()
    [balance.pop(k) for k in list(balance.keys()) if k != 'balances']

    return json.dumps(balance["balances"])




# api_key = 'UimWOZ9hTGnsH1K2iIad65HcDCM0wMcvhpV8i7WzhxKyT17s3CDk4YLEZIsRJfBM'
# api_secret = 'XVtmEKyTUeP3hxw6xmWjWWWWf2DWPSgyQXxSFrrQMt3TjL8vYGryyjzLBiYfQYa3'