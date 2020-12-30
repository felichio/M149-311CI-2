db.requests.aggregate([
    {$match: {$and: [{creation_date: {$gte: ISODate("2015-04-08")}}, {creation_date: {$lte: ISODate("2015-04-30")}}, {completion_date: {$ne: ""}}]}}, 
    {$group: {_id: "$type_of_service_request", avgdays: {$avg: {$subtract: ["$completion_date", "$creation_date"]}}}}, 
    {$project: {type: "$_id", _id: 0, avg_days: {$divide: ["$avgdays", 100 * 3600 * 24]}}}, 
    {$sort: {avg_days: -1}}
])


// Two Days are parameters