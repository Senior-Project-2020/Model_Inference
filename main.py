from helpers.api import API
from helpers.model import Model
import pandas as pd

def main():
    model = Model(model_file='models/Model.h5', scaler_file='models/scaler.pkl')
    api = API()

    companies = pd.read_json('models/companies.json')

    for company in companies.loc[:, 'Symbol']:
        prediction = model.predict_tomorrow(company)
        opening = 0 # Insert tomorrow opening here

        response = api.submit_prediction(company, opening, prediction)
        if response.status_code in [200, 201]:
            print("Creation Successful")
        else:
            print("Unsuccessful")

    return

if __name__ == '__main__':
    main()
