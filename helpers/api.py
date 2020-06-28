import os
import requests
from datetime import date

class API():
    def __init__(self):
        self._host = 'http://54.198.60.36/api/v1/'
        self._date = date.today()

    def submit_prediction(self, ticker_symbol, opening_price, prediction_value):
        endpoint = 'stock-price/'

        header = {
            'Authorization': os.environ['API_KEY'],
        }

        params = {
            'stock': ticker_symbol,
            'date': str(self._date),
            'opening_price': opening_price,
            'predicted_closing_price': prediction_value
        }

        return requests.post(url=os.path.join(self._host, endpoint), data=params, headers=header)
