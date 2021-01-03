from pymongo import MongoClient
from bson.objectid import ObjectId
import json




def get_three_least_common_wards_per_type(db, type):
    result = db.requests.aggregate([
        {"$match": {"type_of_service_request": type}}, 
        {"$group": {"_id": "$ward", "count": {"$sum": 1}}}, 
        {"$sort": {"count": 1}}, 
        {"$project": {"_id": 0, "ward": "$_id", "count": "$count"}},
        {"$match": {"ward": {"$ne": None}}},
        {"$limit": 3}
    ])

    return json.dumps(list(result))


# print(get_three_least_common_wards_per_type("Graffiti Removal"))