db.requests.aggregate([
    {$match: {$and: [{creation_date: ISODate("2015-04-13T00:00:00Z")}, {zip_code: {$ne: ""}}]}}, 
    {$group: {_id: {zip: "$zip_code", type: "$type_of_service_request"}, hits: {$sum: 1}}}, 
    {$sort: {"_id.zip": -1, hits: -1}}, 
    {$group: {_id: "$_id.zip", per_zip: {$push: {type: "$_id.type", hits: "$hits"}}}}, 
    {$project: {_id: 0, zip_code: "$_id", topThreeTypes: {$slice: ["$per_zip", 0, 3]}}} 
])

// Date is parameter