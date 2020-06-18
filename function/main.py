import json
from helpers.api import API
from helpers.model import Model
import pandas as pd
import os

def main():
    # api_key = os.environ['API_KEY']

    companies = pd.read_json('models/companies.json')
    print(companies)
    model = Model(model_file='models/Model.h5', scaler_file='models/scaler.pkl')

    for company in companies.loc[:, 'Symbol']:
        print(f"Tomorrow's prediction for {company} is: {model.predict_tomorrow(company)}")

    return

if __name__ == '__main__':
    main()
