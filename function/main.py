import json
import boto3
from function.helpers.api import API
import pandas as pd
import os

def main():
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )
    api_key = ''

    try:
        api_key = client.get_secret_value(
            SecretId='API_key'
        )
    except Exception:
        pass
    
    return {
        'statusCode': 200,
        'body': api_key
    }

if __name__ == '__main__':
    main()
