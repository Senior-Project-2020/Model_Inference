from helpers.api import API
from helpers.model import Model
from helpers.stock import StockCollection
import pandas as pd

def main():
    model = Model(model_file='models/Model.h5', scaler_file='models/scaler.pkl')
    api = API()

    companies = pd.read_json('models/companies.json')

    for company in companies.loc[:, 'Symbol']:
        prediction = model.predict_tomorrow(company)

        stock = StockCollection(company)
        high, low, open_price, close_price, volume = stock.get_yesterday_data()
        
        update_response = api.update_previous_day(company, high, low, open_price, close_price, volume)
        create_response = api.submit_prediction(company, prediction)
        
        print(f'Stock: {company} Update reponse: {update_response.status_code} Create response: {create_response.status_code}')

    return

if __name__ == '__main__':
    main()
