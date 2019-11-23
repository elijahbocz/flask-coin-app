from app import app
import requests
import json
from flask import render_template, url_for, redirect
from app.scripts.getters.coins_markets import get_bulk
from app.scripts.getters.coin_detailed import get_coin_data
from app.forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    bulk = get_bulk()
    return render_template('index.html', title='Coinz', data=bulk)


@app.route('/about')
def about():
    return render_template('about.html', title='About This App')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        coin = form.input.data
        return redirect(url_for('.search_coin', coin=coin))
    return render_template('search.html', form=form)


@app.route('/search/<coin>')
def search_coin(coin):
    coin_data = get_coin_data(coin)
    return render_template('search_result.html', coin_data=coin_data)
