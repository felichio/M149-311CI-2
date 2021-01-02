from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

requests = db.requests


def get_three_most_common_types_per_zip(start_date):
    result = requests.aggregate([
        {"$match": {"$expr": {"$eq": ["$creation_date", {"$dateFromString": {"dateString": start_date}}]}}}, 
        {"$group": {"_id": {"zip": "$zip_code", "type": "$type_of_service_request"}, "hits": {"$sum": 1}}}, 
        {"$sort": {"_id.zip": -1, "hits": -1}}, 
        {"$group": {"_id": "$_id.zip", "per_zip": {"$push": {"type": "$_id.type", "hits": "$hits"}}}}, 
        {"$project": {"_id": 0, "zip_code": "$_id", "top_three_types": {"$slice": ["$per_zip", 0, 3]}}} 
    ])

    return json.dumps(list(result))


# print(get_three_most_common_types_per_zip("2015-04-08"))