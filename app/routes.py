from app import app
import requests
import json
from flask import render_template
from app.scripts.getters.coins_markets import get_bulk


@app.route('/')
@app.route('/index')
def index():
    bulk = get_bulk()
    return render_template('index.html', title='Coinz', data=bulk)

@app.route('/about')
def about():
    return render_template('about.html', title='About This App')