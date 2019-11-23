from app import app
import requests
import json
from flask import render_template
from app.scripts.getters.coins_markets import get_names_and_prices


@app.route('/')
@app.route('/index')
def index():
    names_and_prices = get_names_and_prices()
    return render_template('index.html', title='Coinz', names_and_prices=names_and_prices)

@app.route('/about')
def about():
    return render_template('about.html', title='About This App')