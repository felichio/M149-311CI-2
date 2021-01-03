import requests
import json
from bson.objectid import ObjectId

#5feeef7e60a4acba8786e641

request_id = "5feefde8f884f9ccd91e3094"
citizen_id = "5ff082b06d74c9911f89577e"

#name Daniel David

#ObjectId("5fef95821367f7591b820cb4") -> citizen
#ObjectId("5fef0572f884f9ccd946e41e") -> req
r = requests.post(f"http://localhost:5000/upvote/{request_id}", headers = {"Content-Type": "application/json"}, data = json.dumps({"citizen_id": citizen_id}))

print(r.text)