import requests

url = "https://api.ipgeolocation.io/ipgeo?apiKey=a2ad3b90bfed4832bc40274215c90bfc&ip=77.21.217.177"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
