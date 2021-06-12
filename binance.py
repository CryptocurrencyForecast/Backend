from requests import Request, Session
import json

url = 'https://api.binance.com/api/v3/exchangeInfo'

session = Session()

response = session.get(url)
data = json.loads(response.text)

cryptos = list(set([cryto['baseAsset'] for cryto in data['symbols']]))
print(len(cryptos))

for cryto in cryptos:
    print(cryto)
