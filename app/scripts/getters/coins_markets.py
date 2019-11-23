import json
import requests
from app.scripts.getters.coins_list import get_coin_ids

ids = get_coin_ids()


def fetch_us_markets():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "a1284238-2e65-4030-8f41-51af2070db16",
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return data


def get_names_and_prices():
    data = fetch_us_markets()

    names_and_prices = []
    for element in data:
        names_and_prices.append((element['name'], element['current_price']))
    return names_and_prices

get_names_and_prices()
