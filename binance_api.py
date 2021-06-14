from binance.client import Client
import json
import requests


def get_account_balance(token):
    # Testnet config
    api_key = token[:64]
    api_secret = token[64:]
    client = Client(api_key, api_secret, testnet=True)

    # Loading balances
    balance = client.get_account()
    [balance.pop(k) for k in list(balance.keys()) if k != 'balances']

    # Price per asset in binance API
    for i in range(len(balance["balances"])):
        crypto = balance['balances'][i]['asset']
        if crypto != "USDT":
            binance_url="https://api.binance.com/api/v3/avgPrice?symbol="+ crypto +"USDT"

        data=requests.get(url=binance_url).json()

        if balance["balances"][i]["asset"] == "USDT" :
            balance["balances"][i]["value"]=(str(1*float(balance["balances"][i]["free"])))
        else :
            balance["balances"][i]["value"]=(str(float(data['price'])*float(balance["balances"][i]["free"])))
    print (json.dumps(balance["balances"]))
    return json.dumps(balance["balances"])
    
# Test net keys (dummy network)
# api_key = 'UimWOZ9hTGnsH1K2iIad65HcDCM0wMcvhpV8i7WzhxKyT17s3CDk4YLEZIsRJfBM'
# api_secret = 'XVtmEKyTUeP3hxw6xmWjWWWWf2DWPSgyQXxSFrrQMt3TjL8vYGryyjzLBiYfQYa3'