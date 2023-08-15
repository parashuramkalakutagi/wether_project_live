import csv

import requests
import json

url = "http://127.0.0.1:8000/WeatherCSV/"

payload = json.dumps({
  "temp__lt": 200
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response)