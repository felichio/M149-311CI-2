import requests

r = requests.get("http://localhost:5000/query/10")

print(r.text)