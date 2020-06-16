import os
import requests

class API():
    def __init__(self):
        self._host = ''

    def submit_prediction(self, ticker_symbol, prediction_value):
        endpoint = '/predictions'

        params = {
            'symbol': ticker_symbol,
            'prediction': prediction_value
        }

        requests.post(url=os.path.join(self._host, endpoint), params=params)
        pass

    def submit_closing_price(self):
        pass