import json
import requests
from coins_list import get_coin_ids

ids = get_coin_ids()

for item in ids:
    print(item)
    url = "https://api.coingecko.com/api/v3/coins/" + item
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "a1284238-2e65-4030-8f41-51af2070db16",
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    print(data)
