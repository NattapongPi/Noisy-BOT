from requests import Request, Session
import json
import pprint
import os
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from coin_list import coins

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {'symbol': coins, 'convert': 'USD'}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.environ['coin_api_key']
}

session = Session()
session.headers.update(headers)

latest_price = {
    'symbol': '',
    'price': '',
    'percent_change_24h': '',
    'percent_change_7d': ''
}


def get_latest_price(response=None, symbol=None):
    try:
        if response is None:
            response = session.get(url, params=parameters)
        latest_price['symbol'] = json.loads(
            response.text)['data'][symbol]['symbol']
        latest_price['price'] = json.loads(
            response.text)['data'][symbol]['quote']['USD']['price']
        latest_price['percent_change_24h'] = json.loads(
            response.text
        )['data'][symbol]['quote']['USD']['percent_change_24h']
        latest_price['percent_change_7d'] = json.loads(
            response.text)['data'][symbol]['quote']['USD']['percent_change_7d']
        return latest_price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e


def get_all_latest_price():
    response = session.get(url, params=parameters)
    data = []
    _symbol = parameters['symbol'].split(',')
    for s in _symbol:
        data.append(get_latest_price(response, s).copy())
    return data
