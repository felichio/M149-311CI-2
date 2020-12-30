from pymongo import MongoClient
from bson.objectid import ObjectId
from faker import Faker
import constant


client = MongoClient()

db = client.chicago_incidents

citizens = db.citizens
requests = db.requests


fake = Faker()
Faker.seed(0)

# clear citizen collection
citizens.delete_many({})

#clear requests upvoted_by field
requests.update_many({}, {"$unset": {"upvoted_by": ""}})



def create_citizens(n):
    data = []
    for i in range(n):
        data.append({"name": fake.name(), "telephone": fake.phone_number(), "address": fake.address()})
    result = citizens.insert_many(data)
    print("Inserted successfully " + str(len(result.inserted_ids)) + " number of citizens")
    


create_citizens(constant.NUM_OF_CITIZENS)






