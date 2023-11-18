import requests
import time

response = requests.post(
    "http://127.0.0.1:5000/add", json={"key": "134.lols", "value": "5180"}
)

print(response)
if response.status_code == 200:
    print("Retrieved IP: ")
    print(response.json())


time.sleep(2)

response = requests.post(
    "http://127.0.0.1:5000/del", json={"key": "134.lols", "value": "5180"}
)

print(response)
if response.status_code == 200:
    print("Retrieved IP: ")
    print(response.json())


time.sleep(2)

response = requests.post(
    "http://127.0.0.1:5000/add", json={"key": "134.lols", "value": "5120"}
)

print(response)
if response.status_code == 200:
    print("Retrieved IP: ")
    print(response.json())


time.sleep(2)

response = requests.post(
    "http://127.0.0.1:5000/del", json={"key": "1345lols", "value": "5180"}
)

print(response)
if response.status_code == 200:
    print("Retrieved IP: ")
    print(response.json())


time.sleep(2)

response = requests.post(
    "http://127.0.0.1:5000/del", json={"key": "135.lols", "value": "5180"}
)

print(response)
if response.status_code == 200:
    print("Retrieved IP: ")
    print(response.json())


time.sleep(2)

response = requests.post(
    "http://127.0.0.1:5000/add", json={"key": "134.lols", "value": "5180"}
)

print(response)
if response.status_code == 200:
    print("Retrieved IP: ")
    print(response.json())
