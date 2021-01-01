from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

requests = db.requests


def get_total_request_per_day(start_date, end_date, type):
    result = requests.aggregate([
        {"$match": {"type_of_service_request": type}}, 
        {"$match": {"$expr": {"$and": [{"$gte": ["$creation_date", {"$dateFromString": {"dateString": start_date}}]}, {"$lte": ["$creation_date", {"$dateFromString": {"dateString": end_date}}]}]}}}, 
        {"$group": {"_id": {"type": "$type_of_service_request", "creation": "$creation_date"}, "totalRequests": {"$sum": 1}}},
        {"$project": {"_id": 0, "type": "$_id.type", "creation_date": {"$dateToString": {"date": "$_id.creation"}}, "total_requests": "$totalRequests"}},
        {"$sort": {"creation_date": 1}}
    ])

    return json.dumps(list(result))


print(get_total_request_per_day("2015-04-08", "2016-04-30", "Tree Trim"))