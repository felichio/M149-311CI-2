import requests


r = requests.get("http://localhost:5000/query/7", params = {"start_date": "2015-04-01"})

print(r.text)