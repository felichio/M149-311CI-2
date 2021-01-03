from pymongo import MongoClient
from bson.objectid import ObjectId
import json



def get_fifty_most_active_citizens(db):
    result = db.citizens.aggregate([
        {"$match": {"upvotes": {"$exists": True}}}, 
        {"$project": {"_id": {"$toString": "$_id"}, "name": 1, "num_of_upvotes": {"$size": "$upvotes"}}}, 
        {"$sort": {"num_of_upvotes": -1}}, 
        {"$limit": 50}
])

    return json.dumps(list(result))


# print(get_fifty_most_active_citizens())