from binance.client import Client
print("teeeetetetetteet")
# API Key: UimWOZ9hTGnsH1K2iIad65HcDCM0wMcvhpV8i7WzhxKyT17s3CDk4YLEZIsRJfBM
# Secret Key: XVtmEKyTUeP3hxw6xmWjWWWWf2DWPSgyQXxSFrrQMt3TjL8vYGryyjzLBiYfQYa3

api_key = 'UimWOZ9hTGnsH1K2iIad65HcDCM0wMcvhpV8i7WzhxKyT17s3CDk4YLEZIsRJfBM'
api_secret = 'XVtmEKyTUeP3hxw6xmWjWWWWf2DWPSgyQXxSFrrQMt3TjL8vYGryyjzLBiYfQYa3'

client = Client(api_key, api_secret, testnet=True)

info = client.get_all_tickers()
print(info)