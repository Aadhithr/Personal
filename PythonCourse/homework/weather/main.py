import requests

api = "DoBZihLC0L9BI9F91B6O6QpXGAoFBNTE"
location="newyork"
url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&timesteps=2023-04-30&apikey={api}"



headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

data = response.json()


for x in data():
    print(x)