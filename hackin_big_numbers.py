import time
import requests
import json
import pandas as pd

base_url = "http://116.202.111.229:8000"
api_key = "VPLrVk4hSZMdGrW2wAP0GTpsV2Jsdx5Z"

headers = {"x-api-key": api_key}

rounds = 5
current_round = 1
examples = []
while True:
    # Get a new hint for current company or get the first hint for a new company after calling /evaluate/reset

    tmp_dict = {}
    tmp_company_id = None
    while current_round != 6:
        response = requests.get(f"{base_url}/evaluate/hint", headers=headers)

        print(response.status_code, response.json())

        obj_hint = response.json()

        if tmp_company_id is None:
            tmp_company_id = obj_hint["company_id"]

        if tmp_company_id != obj_hint["company_id"]:
            current_round = 1
            tmp_dict = {}
            tmp_company_id = None

        # predict based off given hint
        time.sleep(1)

        # Post your answer for current hint
        data = {"answer": "abstain"}
        response = requests.post(
            f"{base_url}/evaluate/answer", json=data, headers=headers
        )

        print(response.status_code, response.json())

        obj_eval = response.json()

        if tmp_dict:
            tmp_dict.update(
                {
                    "round_" + str(current_round): obj_hint["hint"],
                }
            )
        else:

            tmp_dict = {
                "company_id": obj_hint["company_id"],
                "round_" + str(current_round): obj_hint["hint"],
                "answer": obj_eval["answer"],
            }

        print(current_round)
        print(tmp_dict)

        # print keys of response.json()
        # for key in response.json().keys():
        #     print(key)

        print("")

        current_round = current_round + 1
        time.sleep(1)

    print(tmp_dict)

    with open(
        "companies/" + str(tmp_dict["company_id"]) + ".json", "w", encoding="utf-8"
    ) as f:
        json.dump(tmp_dict, f, ensure_ascii=False, indent=4)

    examples.append(tmp_dict)
    tmp_df = pd.DataFrame(examples)
    tmp_df.to_csv("companies/data.csv")
    print(
        "----------------------------------------------------------------------------\n"
    )

    # Get hints about a new company
    current_round = 1
    response = requests.get(f"{base_url}/evaluate/reset", headers=headers)

    print(response.status_code, response.json())

    # sleep 5 min and 10 seconds
    time.sleep(3)  # 5 min 10 sec
