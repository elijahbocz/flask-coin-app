import json
import requests


def fetch_coins_list():
    url = "https://api.coingecko.com/api/v3/coins/list"

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "a1284238-2e65-4030-8f41-51af2070db16"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return data


def get_coin_ids():
    data = fetch_coins_list()

    ids = []
    for element in data:
        ids.append(element['id'])

    return ids


def get_coin_symbols():
    data = fetch_coins_list()

    symbols = []
    for element in data:
        symbols.append(element['symbol'])

    return symbols


def get_coin_names():
    data = fetch_coins_list()

    names = []
    for element in data:
        names.append(element['name'])

    return names


def get_coin_id_by_name(coin_name):
    data = fetch_coins_list()
    coin_id = ''
    for element in data:
        if str(coin_name).lower() == str(element['name']).lower():
            coin_id = element['id']
    return coin_id


