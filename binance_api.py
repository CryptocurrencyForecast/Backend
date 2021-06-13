from binance.client import Client
import json

# TESTNET CONFIG
api_key = 'UimWOZ9hTGnsH1K2iIad65HcDCM0wMcvhpV8i7WzhxKyT17s3CDk4YLEZIsRJfBM'
api_secret = 'XVtmEKyTUeP3hxw6xmWjWWWWf2DWPSgyQXxSFrrQMt3TjL8vYGryyjzLBiYfQYa3'
client = Client(api_key, api_secret, testnet=True)

# Loading balances
balance = client.get_account()
[balance.pop(k) for k in list(balance.keys()) if k != 'balances']

b_json = json.dumps(balance)
print(b_json)
