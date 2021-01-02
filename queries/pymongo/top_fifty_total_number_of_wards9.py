from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens
requests = db.requests

def get_top_fifty_total_number_of_wards():
    result = requests.aggregate([ 
        {"$project": {"_id": 1, "ward": 1, "upvoted_by": 1}}, 
        {"$unwind": "$upvoted_by" }, 
        {"$group":{"_id":{"up":"$upvoted_by","ward": "$ward"}}}, 
        {"$match": {"_id.ward": {"$ne": None}}}, 
        {"$group":{"_id":"$_id.up","total":{"$sum":1}}},
        {"$project": {"_id": {"$toString": "$_id"}, "total": "$total"}},
        {"$sort": {"total": -1}}, 
        {"$limit": 50}
    ])

    return json.dumps(list(result))


# print(get_top_fifty_total_number_of_wards())