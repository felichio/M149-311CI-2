import requests
import json

r = requests.post("http://localhost:5000/query/6", headers = {"Content-Type": "application/json"}, data = json.dumps({"start_date": "2015-04-01", "bottom_left": [-88.023555, 41.548756], "up_right": [-87.770997, 41.886956]}))

print(r.text)