from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens


def get_wards_name_has_casted_a_vote(name):
    result = citizens.aggregate([
        {"$match": {"name": name}},
        {"$lookup": {"from": "requests", "localField": "upvotes", "foreignField": "_id", "as": "upvotes"}},
        {"$project": {"_id": 1, "name": 1, "wards": "$upvotes.ward"}},
        {"$project": {"_id": {"$toString": "$_id"}, "name": 1, "wards": {"$setIntersection": ["$wards"]}}}
    ])

    return json.dumps(list(result))


# print(get_wards_name_has_casted_a_vote("Norma Fisher"))