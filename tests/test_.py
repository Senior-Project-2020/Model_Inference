from unittest import TestCase
from function.helpers.stock import StockCollection
from function.helpers.model import Model

class StockCollectionTests(TestCase):
    def setUp(self):
        super().setUp()
        self.collection = StockCollection('MSFT')

    def test_collection_dataframe_value_exitsts(self):
        dataframe = self.collection.get_dataframe()
        assert dataframe is not None
        assert dataframe.shape[1] == 13

    def test_collection_dataframe_has_correct_featues(self):
        dataframe = self.collection.get_dataframe()
        assert list(dataframe.columns) == [
            'Open', 'High', 'Low', 'Close', 'Volume', 'Year', 'Month', 'Day',
            'Range', 'Change in Close', 'Change in Low', 'Change in High',
            'Change in Volume'
        ]


class ModelTests(TestCase):
    def setUp(self):
        super().setUp()
        self.model = Model("function/models/Model.h5", "function/models/scaler.pkl")
    
    def test_predict_tomorrow(self):
        prediction = self.model.predict_tomorrow('MSFT')
        assert prediction.shape == (1,)
