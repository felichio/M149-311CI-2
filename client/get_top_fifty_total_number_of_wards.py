import requests


r = requests.get("http://localhost:5000/query/9")

print(r.text)