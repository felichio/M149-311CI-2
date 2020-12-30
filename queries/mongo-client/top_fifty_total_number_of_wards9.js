db.citizens.aggregate([
    {$lookup: {from: "requests", localField: "upvotes", foreignField: "_id", as: "upvotes"}}, 
    {$project: {_id: 1, name: 1, wards: "$upvotes.ward"}}, 
    {$project: {_id: 1, name: 1, wards: {$size: {$setIntersection: ["$wards"]}}}}, 
    {$sort: {wards: -1}}, 
    {$limit: 50}
])

// Slow, need better implementation