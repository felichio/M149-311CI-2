from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()

db = client.chicago_incidents

requests = db.requests


def get_three_least_common_wards_per_type(type):
    result = requests.aggregate([
        {"$match": {"type_of_service_request": type}}, 
        {"$group": {"_id": "$ward", "count": {"$sum": 1}}}, 
        {"$sort": {"count": 1}}, 
        {"$project": {"_id": 0, "ward": "$_id", "count": "$count"}}, 
        {"$limit": 3}
    ])

    return json.dumps(list(result))


print(get_three_least_common_wards_per_type("Graffiti Removal"))