import requests

r = requests.get("http://localhost:5000/query/11", params = {"name": "Norma Fisher"})

print(r.text)