import yfinance as yf
import pandas as pd

class StockCollection:
    def __init__(self, symbol):
        self._ticker = yf.Ticker(symbol)

    def _remove_null_rows(self, data):
        '''
        Remove null rows from data

        Args:
            data (pd.DataFrame): data to remove null rows from
        
        Returns:
            pd.DataFrame: the same dataframe without null rows removed
        '''
        null_columns=data.columns[data.isnull().any()]
        null_rows = data[data.isnull().any(axis=1)][null_columns].index
        return data.drop(null_rows).reset_index(drop=True)

    def get_dataframe(self):
        dataframe = pd.DataFrame(self._ticker.history()).drop(columns=['Stock Splits', 'Dividends']).reset_index()

        dataframe.loc[:, 'Year'] = pd.DatetimeIndex(dataframe['Date']).year
        dataframe.loc[:, 'Month'] = pd.DatetimeIndex(dataframe['Date']).month
        dataframe.loc[:, 'Day'] = pd.DatetimeIndex(dataframe['Date']).weekday
        dataframe.loc[:, 'Range'] = dataframe.loc[:, 'High'] - dataframe.loc[:, 'Low']
        dataframe.loc[:, 'Change in Close'] = dataframe.loc[:, 'Close'] - dataframe.loc[:, 'Close'].shift(1)
        dataframe.loc[:, 'Change in Low'] = dataframe.loc[:, 'Low'] - dataframe.loc[:, 'Low'].shift(1)
        dataframe.loc[:, 'Change in High'] = dataframe.loc[:, 'High'] - dataframe.loc[:, 'High'].shift(1)
        dataframe.loc[:, 'Change in Volume'] = dataframe.loc[:, 'Volume'] - dataframe.loc[:, 'Volume'].shift(1)

        return self._remove_null_rows(dataframe).drop(columns=['Date'])
