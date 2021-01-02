import requests

r = requests.get("http://localhost:5000/query/5", params = {"start_date": "2015-04-01", "end_date": "2015-04-30"})

print(r.text)