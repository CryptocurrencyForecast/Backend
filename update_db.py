import requests
import json
import time

# Liste URL API access
nomics_url_RAW = "https://api.nomics.com/v1/markets?key=f40c6b7456c197028c38acdd0a2b6c23&exchange=binance&quote=BTC"
binance_url_RAW = "https://api.binance.com/api/v3/exchangeInfo"

# Variables
cryptosListBinance = []
cryptosListNomics = ""
maxMarketCap = 120000000
minMarketCap = 40000000
pctChangement = 50

# Calculs variables
pctChangement = pctChangement / 100

# Sessions
session_binance_RAW = requests.Session()
session_nomics_RAW = requests.Session()
session_nomics_COMPLETE = requests.Session()

# Access to Binance Data Raw
response_binance_RAW = session_binance_RAW.get(binance_url_RAW)
data_binance_RAW = json.loads(response_binance_RAW.text)

# Access to Nomics Data Raw
response_nomics_RAW = session_nomics_RAW.get(nomics_url_RAW)
data_nomics_RAW = json.loads(response_nomics_RAW.text)

# Show Binance Data
for crypto in data_binance_RAW['symbols']:
    if (crypto["quoteAsset"] == "BTC" and crypto["status"] == "TRADING"):
        cryptosListBinance.append(crypto["baseAsset"])
# Show Binance Crypto
#print(cryptosListBinance)

# Show Nomics Crypto
for crypto in data_nomics_RAW:
    if crypto["base"] in cryptosListBinance:
        cryptosListNomics += crypto["base"] + ','
# Show Nomics cryptoS
#print(cryptosListNomics)

# Suppression dernière virgule
cryptosListNomics = cryptosListNomics[:-1]

# Création des données finales
nomics_url_COMPLETE = "https://api.nomics.com/v1/currencies/ticker?key=f40c6b7456c197028c38acdd0a2b6c23&ids=" + cryptosListNomics

# Appel de la requête
time.sleep(2)
response_nomics_COMPLETE = session_nomics_COMPLETE.get(nomics_url_COMPLETE)
data_nomics_COMPLETE = json.loads(response_nomics_COMPLETE.text)

# Affichage final
i = 0
for crypto in data_nomics_COMPLETE:
    if (int(crypto["market_cap"]) < maxMarketCap) and (int(crypto["market_cap"]) > minMarketCap):
        i = i+1
        print(str(i) + " : " + crypto["symbol"] + " | " + crypto["market_cap"] + " $")


