from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

requests = db.requests


def get_average_completion_time_per_type(start_date, end_date):
    result = requests.aggregate([
        {"$match": {"$expr": {"$and": [{"$gte": ["$creation_date", {"$dateFromString": {"dateString": start_date}}]}, {"$lte": ["$creation_date", {"$dateFromString": {"dateString": end_date}}]}, {"$ne": ["$completion_date", ""]}]}}}, 
        {"$group": {"_id": "$type_of_service_request", "avgdays": {"$avg": {"$subtract": ["$completion_date", "$creation_date"]}}}}, 
        {"$project": {"type": "$_id", "_id": 0, "avg_days": {"$divide": ["$avgdays", 1000 * 3600 * 24]}}}, 
        {"$sort": {"avg_days": -1}}
    ])

    return json.dumps(list(result))


print(get_average_completion_time_per_type("2015-04-08", "2015-04-30"))