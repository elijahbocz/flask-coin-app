from app import app
import requests
import json
from flask import render_template, url_for, redirect
from app.scripts.getters.coins_markets import get_bulk
from app.scripts.getters.coin_detailed import get_coin_data
from app.scripts.getters.crypto_events import fetch_events
from app.scripts.getters.coin_history import get_coin_history_by_date
from app.forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    bulk = get_bulk()
    return render_template('index.html', title='Coin Directory', data=bulk)


@app.route('/about')
def about():
    return render_template('about.html', title='About This App')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        coin = form.user_input.data
        coin = str(coin).replace(" ", "-").lower()
        return redirect(url_for('.search_coin', coin=coin))
    return render_template('search.html', title='Search Coins', form=form)


@app.route('/search/<coin>', methods=['GET', 'POST'])
def search_coin(coin):
    spaced_coin = str(coin).replace("-", " ")
    coin_data = get_coin_data(spaced_coin)
    return render_template('search_result.html', title=coin_data['name'], coin_data=coin_data, spaced_coin=spaced_coin)


@app.route('/upcoming-events')
def events():
    events_data = fetch_events()
    return render_template('events.html', title='Upcoming Events', data=events_data)
