import os
import requests
from datetime import date

class API():
    def __init__(self):
        self._host = 'http://localhost:8000/api/v1/'
        self._date = date.today()

    def submit_prediction(self, ticker_symbol, opening_price, prediction_value):
        endpoint = 'stock-price/'

        header = {
            'Authorization': 'Token 391a0c42c6866cd8fe8eafa504e554c229738221',
        }

        params = {
            'stock': ticker_symbol,
            'date': str(self._date),
            'opening_price': opening_price,
            'predicted_closing_price': prediction_value
        }

        return requests.post(url=os.path.join(self._host, endpoint), data=params, headers=header)
