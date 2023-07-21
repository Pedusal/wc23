#Fetch WC data

import requests
import pandas as pd

user_email = "test-api@invalid-gmail.com"
password = "password"
def login(user_email, password):
    data = {
        "email": user_email,
        "password": password
    }
    response = requests.post("http://api.cup2022.ir/api/v1/user/login", json=data)
    return response.json()["data"]["token"]

token = login(user_email, password)
base_url = "http://api.cup2022.ir/api/v1/"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

#standings = requests.get(url=base_url + "standings", headers=headers)
response = requests.get(url=base_url + "match", headers=headers)
assert response.status_code == 200

matches_df = pd.DataFrame.from_dict(response.json()["data"])
print(matches_df)



