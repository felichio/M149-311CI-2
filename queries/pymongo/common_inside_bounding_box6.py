from pymongo import MongoClient
from bson.objectid import ObjectId
import json




def get_common_inside_bounding_box(db, bot_left, up_right, start_date):
    result = db.requests.aggregate([
        {"$match": {"$expr": {"$eq": ["$creation_date", {"$dateFromString": {"dateString": start_date}}]}}},
        {"$match": {"location": {"$geoWithin": {"$box": [bot_left, up_right]}}}}, 
        {"$group": {"_id": "$type_of_service_request", "count": {"$sum": 1}}}, 
        {"$sort": {"count": -1}}, 
        {"$limit": 1}
    ])

    return json.dumps(list(result))


# print(get_common_inside_bounding_box6([-88.023555, 41.548756], [-87.770997, 41.886956],"2015-04-30"))