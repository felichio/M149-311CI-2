db.requests.aggregate([
    {$match: {type_of_service_request: "Tree Debris"}}, 
    {$match: {$and: [{creation_date: {$gte: ISODate("2015-04-08")}}, {creation_date: {$lte: ISODate("2015-04-30")}}]}}, 
    {$group: {_id: {type: "$type_of_service_request", creation: "$creation_date"}, totalRequests: {$sum: 1}}}, 
    {$sort: {"_id.creation": 1}}
])


// two Dates and Type_of_service are parameters


// New implementation

db.requests.aggregate([
    {$match: {type_of_service_request: "Tree Debris"}}, 
    {$match: {$expr: {$and: [{$gte: ["$creation_date", {$dateFromString: {dateString: "2015-04-08"}}]}, {$lte: ["$creation_date", {$dateFromString: {dateString: "2015-04-30"}}]}]}}}, 
    {$group: {_id: {type: "$type_of_service_request", creation: "$creation_date"}, totalRequests: {$sum: 1}}},
    {$project: {_id: 0, type: "$_id.type", creation_date: {$dateToString: {date: "$_id.creation"}}, total_requests: "$totalRequests"}},
    {$sort: {"creation_date": 1}}
])