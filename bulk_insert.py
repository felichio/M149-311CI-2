from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import csv
import constant
import re
import math

client = MongoClient()

db = client.chicago_incidents

requests = db.requests
coordinates_pattern = re.compile(r"^[.0-9-]+$")

def fix_row(row, type, names):
    #creation date
    row["creation_date"] = datetime.datetime.strptime(row["creation_date"], '%Y-%m-%dT%H:%M:%S.%f')
    #completion date
    if row["completion_date"] != "":
        row["completion_date"] = datetime.datetime.strptime(row["completion_date"], '%Y-%m-%dT%H:%M:%S.%f')
    #type of service
    row["type_of_service_request"] = constant.types[type]
    #location
    if re.match(coordinates_pattern, row["longitude"]) and re.match(coordinates_pattern, row["latitude"]):
        row["location"] = {"type": "Point", "coordinates": [float(row["longitude"]), float(row["latitude"])]}
    else:
        row["location"] = {"type": "Point", "coordinates": [0, 0]}
    #remove latitude, longitude
    del row["latitude"]
    del row["longitude"]

    for k in list(set(names) & set(constant.int_type)):
        if(row[k]!=""):
            row[k]=int(math.ceil(float(row[k])))
        else:
            del row[k]

    for k in list(set(names) & set(constant.float_type)):
        if(row[k]!=""):
            row[k]=float(row[k])
        else:
            del row[k]        
    
    for k in list(set(names) - set(constant.checked_type)):
        if(row[k]==""):
            del row[k]

    return row


for type in constant.types:
    with open(f"../data/{type}.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        names = csv_reader.fieldnames
        for (index, row) in enumerate(csv_reader):
            requests.insert_one(fix_row(row, type, names))
            print(f"Inserting type: { constant.types[type] }  #{str(index)}")
        print()


    


