import json
import requests
from app.scripts.getters.coins_simple_lists import get_coin_id_by_name
from bs4 import BeautifulSoup


def get_coin_data(coin_name):
    coin_id = get_coin_id_by_name(coin_name)
    url = "https://api.coingecko.com/api/v3/coins/" + coin_id
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "a1284238-2e65-4030-8f41-51af2070db16",
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    soup = BeautifulSoup(data['description']['en'])
    data['description']['en'] = soup.get_text()
    return data
