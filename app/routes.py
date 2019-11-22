from app import app
import requests
import json
from flask import render_template
from app.scripts.getters.coins_list import get_coin_names


@app.route('/')
def index():
    return 'Tessst'


@app.route('/coin')
def coin():
    names = get_coin_names()
    return render_template('coin.html', names=names)