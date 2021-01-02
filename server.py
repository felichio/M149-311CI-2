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
    return get_total_request_per_type(start_date, end_date)


@app.route("/query/2", methods = ["GET"])
def _2():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    type = request.args.get("type")
    # Maybe validation
    print(start_date, end_date, type)
    return get_total_request_per_day(start_date, end_date, type)


@app.route("/query/3", methods = ["GET"])
def _3():
    start_date = request.args.get("start_date")
    # Maybe validation
    print(start_date)
    return get_three_most_common_types_per_zip(start_date)


@app.route("/query/4", methods = ["GET"])
def _4():
    type = request.args.get("type")
    # Maybe validation
    print(type)
    return get_three_least_common_wards_per_type(type)

@app.route("/query/5", methods = ["GET"])
def _5():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    # Maybe validation
    print(start_date, end_date)
    return get_average_completion_time_per_type(start_date, end_date)


@app.route("/query/6", methods = ["POST"])
def _6():
    start_date = request.json.get("start_date")
    bottom_left = request.json.get("bottom_left")
    up_right = request.json.get("up_right")

    # Maybe validation
    print(bottom_left, up_right, start_date)
    
    
    return get_common_inside_bounding_box(bottom_left, up_right, start_date)


@app.route("/query/7", methods = ["GET"])
def _7():
    start_date = request.args.get("start_date")
    # Maybe validation
    print(start_date)
    return get_fifty_most_upvoted_requests(start_date)


@app.route("/query/8", methods = ["GET"])
def _8():
    
    # Maybe validation
    
    return get_fifty_most_active_citizens()


@app.route("/query/9", methods = ["GET"])
def _9():
    
    # Maybe validation
    
    return get_top_fifty_total_number_of_wards()


@app.route("/query/10", methods = ["GET"])
def _10():
    
    # Maybe validation
    
    return get_incident_ids_same_phone()


@app.route("/query/11", methods = ["GET"])
def _11():
    name = request.args.get("name")
    print(name)
    # Maybe validation
    return get_wards_name_has_casted_a_vote(name)