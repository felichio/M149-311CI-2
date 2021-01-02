import requests
import json
from bson.objectid import ObjectId


citizen_id = "5fef95821367f7591b820c62"

r = requests.post(f"http://localhost:5000/citizen/{citizen_id}", headers = {"Content-Type": "application/json"}, data = json.dumps({}))

print(r.text)