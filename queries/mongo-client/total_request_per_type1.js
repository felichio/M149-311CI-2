db.requests.aggregate([
    {$project: {_id: 1, creation_date: 1, type_of_service_request: 1}}, 
    {$match: {$and: [{creation_date: {$gte: ISODate("2015-04-08")}}, {creation_date: {$lte: ISODate("2015-04-30")}}]}}, 
    {$group: {_id: {type: "$type_of_service_request"}, totalRequests: {$sum: 1}}}, 
    {$sort: {totalRequests: -1}}
])

// two Dates are parameters