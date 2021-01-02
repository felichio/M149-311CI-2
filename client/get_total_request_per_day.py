import requests


r = requests.get("http://localhost:5000/query/2", params = {"start_date": "2015-04-01", "end_date": "2015-04-30", "type": "Tree Debris"})

print(r.text)