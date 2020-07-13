import os
import requests
from datetime import date, timedelta
import pandas as pd

class API():
    def __init__(self):
        self._host = 'http://54.198.60.36/api/v1/'
        self._date = date.today()
        self._token = os.environ['API_KEY']
        self._price_list = self.get_price_list()


    def get_price_list(self):
        price_list = pd.DataFrame()
        next_url = os.path.join(self._host, 'stock-price/')

        while(True):
            data = requests.get(
                url=next_url,
                headers={'Authorization': self._token}
            ).json()

            next_url = data['next']
            prices = pd.DataFrame(data['results'])

            price_list = pd.concat((price_list, prices))

            if(next_url == None):
                return price_list

    def submit_prediction(self, ticker_symbol, prediction_value):
        endpoint = 'stock-price/'

        header = {
            'Authorization': self._token,
        }

        params = {
            'stock': ticker_symbol,
            'date': str(self._date),
            'predicted_closing_price': prediction_value
        }

        return requests.post(url=os.path.join(self._host, endpoint), data=params, headers=header)

    def update_previous_day(self, ticker_symbol, high, low, open_price, close_price, volume):
        try:
            delta = timedelta(days=1) if self._date.weekday() != 0 else timedelta(days=3)
            yesterday_id = self._price_list[
                (self._price_list.stock == ticker_symbol) & \
                (self._price_list.date == str(self._date - delta))
            ].iloc[0]['id']
        except Exception:
            yesterday_id = -1

        endpoint = f'stock-price/{yesterday_id}'
        
        header = {
            'Authorization': self._token,
        }

        params = {
            'opening_price' : open_price,
            'actual_closing_price': close_price,
            'daily_high': high,
            'daily_low': low,
            'volume': volume,
        }

        return requests.patch(url=os.path.join(self._host, endpoint), data=params, headers=header)
