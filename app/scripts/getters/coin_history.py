import json
import requests


def get_coin_history_by_date(coin_name, date):
    url = "https://api.coingecko.com/api/v3/coins/" + \
        coin_name + "/history?date=" + date
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "a1284238-2e65-4030-8f41-51af2070db16",
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return data
