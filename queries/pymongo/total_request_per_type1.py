from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

requests = db.requests


def get_total_request_per_type(db, start_date, end_date):
    result = db.requests.aggregate([
        {"$project": {"_id": 1, "creation_date": 1, "type_of_service_request": 1}}, 
        {"$match": {"$expr": {"$and": [{"$gte": ["$creation_date", {"$dateFromString": {"dateString": start_date}}]}, {"$lte": ["$creation_date", {"$dateFromString": {"dateString": end_date}}]}]}}}, 
        {"$group": {"_id": {"type": "$type_of_service_request"}, "total_requests": {"$sum": 1}}},
        {"$project": {"_id": 0, "type": "$_id.type", "total_requests": "$total_requests"}},
        {"$sort": {"total_requests": -1}} 
    ])

    return json.dumps(list(result))


# print(get_total_request_per_type("2015-04-08", "2015-04-30"))