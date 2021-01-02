import requests

r = requests.get("http://localhost:5000/query/8")

print(r.text)