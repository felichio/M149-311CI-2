import requests
import json
from bson.objectid import ObjectId


request_id = "5feefe02f884f9ccd91ebfd5"
citizen_id = "5ff082b06d74c9911f89577e"

r = requests.post(f"http://localhost:5000/downvote/{request_id}", headers = {"Content-Type": "application/json"}, data = json.dumps({"citizen_id": citizen_id}))

print(r.text)