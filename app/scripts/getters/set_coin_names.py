import json
from coins_simple_lists import get_coin_names

coin_names = get_coin_names()

with open('/home/elijah/Code/flask-coin-app/app/scripts/tmp/coin_names.json', 'w') as write_file:
    json.dump(coin_names, write_file)
