import time
import requests
import json
import pandas as pd

base_url = 'http://116.202.111.229:8000'
api_key = 'VPLrVk4hSZMdGrW2wAP0GTpsV2Jsdx5Z'

headers = {
    'x-api-key': api_key
}

rounds = 5
current_round = 1

filename = 'extra_data.csv'
data_columns = ['commercial_name', 'business_tags', 'short_descripti', 'description', 'main_business_category']

df = pd.csv_read(filename, usecols=data_columns)

print(df.head())
exit(0)

while True:
    # Get a new hint for current company or get the first hint for a new company after calling /evaluate/reset
    while current_round != 6:
        response = requests.get(f"{base_url}/evaluate/hint", headers=headers)

        print(response.status_code, response.json())

        # predict based off given hint
        time.sleep(1)


        # Post your answer for current hint
        data = {
            'answer': 'abstain'
        }
        response = requests.post(f"{base_url}/evaluate/answer", json=data, headers=headers)

        print(response.status_code, response.json())
        
        print("")
        
        current_round = current_round + 1
        time.sleep(1)
    
    print("----------------------------------------------------------------------------\n")

    # Get hints about a new company
    current_round = 1
    response = requests.get(f"{base_url}/evaluate/reset", headers=headers)

    print(response.status_code, response.json())
    
    # sleep 5 min and 10 seconds
    time.sleep(300) # 5 min 10 sec
