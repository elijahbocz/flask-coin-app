import json
import requests


def fetch_events():
    url = "https://api.coingecko.com/api/v3/events"
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "a1284238-2e65-4030-8f41-51af2070db16",
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return data
