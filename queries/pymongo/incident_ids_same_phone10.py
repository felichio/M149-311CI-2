from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens


def get_incident_ids_same_phone():
    result = citizens.aggregate([
        {"$group": {"_id": "$telephone", "persons": {"$sum": 1}, "requests": {"$push": "$upvotes"}}},
        {"$match": {"persons": {"$gte": 2}}},
        {"$unwind": "$requests" },
        {"$unwind": "$requests" },
        {"$group": {"_id": {"tel":"$_id","requests":"$requests"}, "num_dup": {"$sum": 1}}},
        {"$match": {"num_dup": {"$gte": 2}}},
        {"$project": {"_id": 0, "telephone": "$_id.tel", "request": {"$toString": "$_id.requests"}, "num_dup": "$num_dup"}}
    ])

    return json.dumps(list(result))


# print(get_incident_ids_same_phone())