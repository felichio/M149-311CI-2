from pymongo import MongoClient
from bson.objectid import ObjectId

import constant
import random

client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens
requests = db.requests


citizens_ids = map(lambda x: x["_id"], citizens.find({}, {"_id": 1}))
requests_ids = list(map(lambda x: x["_id"], requests.find({}, {"_id": 1})))

random.seed(0)

for (index, citizen_id) in enumerate(citizens_ids):
    req_for_upvote = random.sample(requests_ids, random.randrange(0, constant.NUM_OF_UPVOTES + 1))
    citizens.update_one({"_id": citizen_id}, {"$set": {"upvotes": req_for_upvote}})
    for upvoted in req_for_upvote:
        requests.update_one({"_id": upvoted}, {"$push": {"upvoted_by": citizen_id}})
    print("Upvoting process for citizen: " + str(index) + " finished!")


ratio = requests.find({"upvoted_by": {"$exists": True}}).count() / len(requests_ids)

if ratio < (1 / 3):
    print(f"Upvoted Requests must be at least 33.33%. Achieved percentage is {ratio * 100}%. Try increasing the number of citizens!")
else:
    print(f"Conditions are met. Achieved percentage is {ratio * 100}%. Ready for query stage!")
    
