import requests
import json
from bson.objectid import ObjectId


request_id = "5feefd8cf884f9ccd91c3f53"

r = requests.post(f"http://localhost:5000/upvote/{request_id}", headers = {"Content-Type": "application/json"}, data = json.dumps({}))

print(r.text)