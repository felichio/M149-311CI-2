from flask import Flask
from flask import jsonify
from flask import request

from pymongo import MongoClient
from bson.objectid import ObjectId

import sys
sys.path.append("queries/pymongo")

from total_request_per_type1 import get_total_request_per_type
from total_request_per_day2 import get_total_request_per_day
from three_most_common_types_per_zip3 import get_three_most_common_types_per_zip
from three_least_common_wards_per_type4 import get_three_least_common_wards_per_type
from average_completion_time_per_type5 import get_average_completion_time_per_type
from common_inside_bounding_box6 import get_common_inside_bounding_box
from fifty_most_upvoted_requests7 import get_fifty_most_upvoted_requests
from fifty_most_active_citizens8 import get_fifty_most_active_citizens
from top_fifty_total_number_of_wards9 import get_top_fifty_total_number_of_wards
from incident_ids_same_phone10 import get_incident_ids_same_phone
from wards_name_has_casted_a_vote11 import get_wards_name_has_casted_a_vote


client = MongoClient()

db = client.chicago_incidents


citizens = db.citizens
requests = db.requests


app = Flask(__name__)

@app.route("/query/1", methods = ["GET"])
def _1():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    # Maybe validation
    print(start_date, end_date)
    return get_total_request_per_type(db, start_date, end_date)


@app.route("/query/2", methods = ["GET"])
def _2():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    type = request.args.get("type")
    # Maybe validation
    print(start_date, end_date, type)
    return get_total_request_per_day(db, start_date, end_date, type)


@app.route("/query/3", methods = ["GET"])
def _3():
    start_date = request.args.get("start_date")
    # Maybe validation
    print(start_date)
    return get_three_most_common_types_per_zip(db, start_date)


@app.route("/query/4", methods = ["GET"])
def _4():
    type = request.args.get("type")
    # Maybe validation
    print(type)
    return get_three_least_common_wards_per_type(db, type)

@app.route("/query/5", methods = ["GET"])
def _5():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    # Maybe validation
    print(start_date, end_date)
    return get_average_completion_time_per_type(db, start_date, end_date)


@app.route("/query/6", methods = ["POST"])
def _6():
    start_date = request.json.get("start_date")
    bottom_left = request.json.get("bottom_left")
    up_right = request.json.get("up_right")

    # Maybe validation
    print(bottom_left, up_right, start_date)
    
    
    return get_common_inside_bounding_box(db, bottom_left, up_right, start_date)


@app.route("/query/7", methods = ["GET"])
def _7():
    start_date = request.args.get("start_date")
    # Maybe validation
    print(start_date)
    return get_fifty_most_upvoted_requests(db, start_date)


@app.route("/query/8", methods = ["GET"])
def _8():
    
    # Maybe validation
    
    return get_fifty_most_active_citizens(db)


@app.route("/query/9", methods = ["GET"])
def _9():
    
    # Maybe validation
    
    return get_top_fifty_total_number_of_wards(db)


@app.route("/query/10", methods = ["GET"])
def _10():
    
    # Maybe validation
    
    return get_incident_ids_same_phone(db)


@app.route("/query/11", methods = ["GET"])
def _11():
    name = request.args.get("name")
    print(name)
    # Maybe validation
    return get_wards_name_has_casted_a_vote(db, name)


# @app.route("/request/<request_id>", methods = ["POST"])
# def upsert_request(request_id):
#     req_id = ObjectId(request_id)
    

#     return "temp"

# @app.route("/citizen/<citizen_id>", methods = ["POST"])
# def upsert_citizen(citizen_id):
#     cit_id = ObjectId(citizen_id)

#     return "temp"


@app.route("/upvote/<request_id>", methods = ["POST"])
def upvote_request(request_id):
    
    # take citizen id from json payload
    # do upvote logic  <= 1000, 2ble upvoting
    citizen_id = request.json.get("citizen_id")
    
    if not (ObjectId.is_valid(request_id)) or not (ObjectId.is_valid(citizen_id)):
        return jsonify({"error": "Not valid ObjectIds"})
    

    req_id = ObjectId(request_id)
    cit_id = ObjectId(citizen_id)

    result1 = requests.find_one({"_id": req_id})
    result2 = citizens.find_one({"_id": cit_id})

    if not result1:
        return jsonify({"error": "Request not found"})
    if not result2:
        return jsonify({"error": "Citizen not found"})
    

    # check if request already upvoted by citizen
    result = requests.aggregate([
        {"$match": {"_id": req_id}}, 
        {"$match": {"$expr": {"$in": [cit_id, {"$cond": {"if": {"$ifNull": ["$upvoted_by", False]}, "then": "$upvoted_by", "else": []}}]}}}, 
    ])
    
    already_upvoted = len(list(result))
    
    if already_upvoted:
        return jsonify({"error": "Request already upvoted by this citizen"})

    # check if citizen's number of upvotes hit threshold
    result = citizens.aggregate([
        {"$match": {"_id": cit_id}}, 
        {"$project": {"_id": 0, "num_of_upvotes": {"$cond": {"if": {"$ifNull": ["$upvotes", False]}, "then": {"$size": "$upvotes"}, "else": 0}}}}
    ])

    num_of_upvotes = list(result)[0].get("num_of_upvotes")

    if num_of_upvotes > 999:
        return jsonify({"error": "Citizen has reached the maximum number of upvotes"})
    
    
    result1 = citizens.update_one({"_id": cit_id}, {"$addToSet": {"upvotes": req_id}})
    result2 = requests.update_one({"_id": req_id}, {"$addToSet": {"upvoted_by": cit_id}})
    
    return jsonify({"sucess": "Upvoting successful"})


@app.route("/downvote/<request_id>", methods = ["POST"])
def downvote_request(request_id):
    citizen_id = request.json.get("citizen_id")
    
    if not (ObjectId.is_valid(request_id)) or not (ObjectId.is_valid(citizen_id)):
        return jsonify({"error": "Not valid ObjectIds"})
    

    req_id = ObjectId(request_id)
    cit_id = ObjectId(citizen_id)

    result1 = requests.find_one({"_id": req_id})
    result2 = citizens.find_one({"_id": cit_id})

    if not result1:
        return jsonify({"error": "Request not found"})
    if not result2:
        return jsonify({"error": "Citizen not found"})
    

    
    result1 = citizens.update_one({"_id": cit_id}, {"$pullAll": {"upvotes": [req_id]}})
    result2 = requests.update_one({"_id": req_id}, {"$pullAll": {"upvoted_by": [cit_id]}})

    citizens.update_one({"_id": cit_id, "upvotes": []}, {"$unset": {"upvotes": ""}})
    requests.update_one({"_id": req_id, "upvoted_by": []}, {"$unset": {"upvoted_by": ""}})
    
    return jsonify({"sucess": "Downvoting successful"})
    