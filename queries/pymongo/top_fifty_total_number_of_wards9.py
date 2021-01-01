from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens


def get_top_fifty_total_number_of_wards():
    result = citizens.aggregate([
        {"$lookup": {"from": "requests", "localField": "upvotes", "foreignField": "_id", "as": "upvotes"}}, 
        {"$project": {"_id": 1, "name": 1, "wards": "$upvotes.ward"}}, 
        {"$project": {"_id": {"$toString": "$_id"}, "name": 1, "wards": {"$size": {"$setIntersection": ["$wards"]}}}}, 
        {"$sort": {"wards": -1}}, 
        {"$limit": 50}
    ])

    return json.dumps(list(result))


print(get_top_fifty_total_number_of_wards())