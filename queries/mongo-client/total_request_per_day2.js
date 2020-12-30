db.requests.aggregate([
    {$match: {type_of_service_request: "Tree Debris"}}, 
    {$match: {$and: [{creation_date: {$gte: ISODate("2015-04-08")}}, {creation_date: {$lte: ISODate("2015-04-30")}}]}}, 
    {$group: {_id: {type: "$type_of_service_request", creation: "$creation_date"}, totalRequests: {$sum: 1}}}, 
    {$sort: {"_id.creation": 1}}
])


// two Dates and Type_of_service are parameters