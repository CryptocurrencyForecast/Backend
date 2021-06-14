import requests
import json


def get_information_nomics(token):

    url = "https://api.nomics.com/v1/currencies?key=f40c6b7456c197028c38acdd0a2b6c23&ids=" + token
    data = requests.get(url=url).json()
    return json.dumps(data)
