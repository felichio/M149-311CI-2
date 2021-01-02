import requests


r = requests.get("http://localhost:5000/query/4", params = {"type": "Graffiti Removal"})

print(r.text)