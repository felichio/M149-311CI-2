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
        {"$project": {"_id": 1, "persons": 1, "requests": 1, "requests_temp": {"$reduce": {"input": "$requests", "initialValue": [], "in": {"$concatArrays": ["$$value", "$$this"]}}}}}, 
        {"$project": {"_id": 1, "persons": 1, "requests": {"$reduce": {"input": "$requests", "initialValue": "$requests_temp", "in": {"$setIntersection": ["$$value", "$$this"]}}}}}, 
        {"$project": {"_id": 1, "persons": 1, "requests": {"$map": {"input": "$requests", "as": "t", "in": {"$toString": "$$t"}}}}}
    ])

    return json.dumps(list(result))


print(get_incident_ids_same_phone())