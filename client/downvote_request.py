import requests
import json
from bson.objectid import ObjectId


request_id = "5ff1fdbdbb85722936e804b2"
citizen_id = "5ff21576e2731dc89d2d3a23"

r = requests.post(f"http://localhost:5000/downvote/{request_id}", headers = {"Content-Type": "application/json"}, data = json.dumps({"citizen_id": citizen_id}))

print(r.text)