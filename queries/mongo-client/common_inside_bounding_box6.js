// First add geo index
db.requests.createIndex({location: "2dsphere"})



db.requests.aggregate([
    {$match: {$and: [{location: {$geoWithin: {$box: [[-88.023555, 41.548756], [-87.770997, 41.886956]]}}}, {creation_date: {$eq: ISODate("2015-04-30")}}]}}, 
    {$group: {_id: "$type_of_service_request", count: {$sum: 1}}}, 
    {$sort: {count: -1}}, 
    {$limit: 1}
])

// Bottom left, Upper right box coordinates (lon, lat), date are parameters


// New implementation

db.requests.aggregate([
    {$match: {$expr: {$eq: ["$creation_date", {$dateFromString: {dateString: "2015-04-30"}}]}}},
    {$match: {location: {$geoWithin: {$box: [[-88.023555, 41.548756], [-87.770997, 41.886956]]}}}}, 
    {$group: {_id: "$type_of_service_request", count: {$sum: 1}}}, 
    {$sort: {count: -1}}, 
    {$limit: 1}
])