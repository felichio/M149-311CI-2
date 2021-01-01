from pymongo import MongoClient
from bson.objectid import ObjectId



client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens
requests = db.requests

names_streets = [("Petsinis Petros", "random avenue 67"), ("Safaridis Felix", "random avenue 38")]
tel = "+302107275161"

def insert_citizens(names_streets, tel):
    ids = []
    for e in names_streets:
        ids.append(db.citizens.insert_one({"name": e[0], "telephone": tel, "address": e[1]}).inserted_id)
    return ids

citizens_ids = insert_citizens(names_streets, tel)
requests_ids = list(map(lambda x: x["_id"], requests.find({"upvoted_by": {"$exists": True}})))



for (index, citizen_id) in enumerate(citizens_ids):
    req_for_upvote = []
    for i in range(5):
        req_for_upvote.append(requests_ids[i + index])
    citizens.update_one({"_id": citizen_id}, {"$set": {"upvotes": req_for_upvote}})
    for upvoted in req_for_upvote:
        requests.update_one({"_id": upvoted}, {"$push": {"upvoted_by": citizen_id}})
    print("Upvoting process for citizen: " + str(index) + " finished!")