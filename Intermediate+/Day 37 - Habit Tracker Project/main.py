import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fnkjnashfbanasjndfqio"
USERNAME = "rohiradhruv"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graphId = "graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": graphId,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today_date = datetime.now().strftime("%Y%m%d")
entry_endpoint = f"{graph_endpoint}/{graphId}"
entry_params = {
    "date": today_date,
    "quantity": input("How many kilometres did you cycle today?: "),
}
response = requests.post(url=entry_endpoint, headers=headers, json=entry_params)
print(response.text)

update_endpoint = f"{entry_endpoint}/{today_date}"
update_params = {
    "quantity": "14"
}
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)

