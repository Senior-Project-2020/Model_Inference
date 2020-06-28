import tensorflow as tf
from pickle import load
from helpers.stock import StockCollection

class Model():
    "Class to represent a tensorflow model"

    def __init__(self, model_file, scaler_file):
        self._model = tf.keras.models.load_model(model_file)
        self._scaler = load(open(scaler_file, 'rb'))
        
    def predict_tomorrow(self, symbol):
        collection = StockCollection(symbol)
        data = collection.get_dataframe()
        data = self._scaler.transform(data)

        prediction = self._model.predict(data)
        return round(float(prediction[-1]), 2)

    def get_next_opening(self, symbol):
        collection = StockCollection(symbol)
        data = collection.get_dataframe()
        return data.iloc[-1, 5]
