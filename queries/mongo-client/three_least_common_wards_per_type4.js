db.requests.aggregate([
    {$match: {type_of_service_request: "Graffiti Removal"}}, 
    {$group: {_id: "$ward", count: {$sum: 1}}}, 
    {$sort: {count: 1}}, 
    {$project: {_id: 0, ward: "$_id", count: "$count"}},
    {$match: {ward: {$ne: null}}},
    {$limit: 3}
])



// Type is parameter