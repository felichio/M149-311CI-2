db.citizens.aggregate([
    {$lookup: {from: "requests", localField: "upvotes", foreignField: "_id", as: "upvotes"}}, 
    {$project: {_id: 1, name: 1, wards: "$upvotes.ward"}}, 
    {$project: {_id: 1, name: 1, wards: {$size: {$setIntersection: ["$wards"]}}}}, 
    {$sort: {wards: -1}}, 
    {$limit: 50}
])

// Slow, need better implementation

// Index

db.requests.createIndex({upvoted_by: -1})

// New implementation ObjectId to String

db.citizens.aggregate([
    {$lookup: {from: "requests", localField: "upvotes", foreignField: "_id", as: "upvotes"}}, 
    {$project: {_id: 1, name: 1, wards: "$upvotes.ward"}}, 
    {$project: {_id: {$toString: "$_id"}, name: 1, wards: {$size: {$setIntersection: ["$wards"]}}}}, 
    {$sort: {wards: -1}}, 
    {$limit: 50}
])


// New new Implementation

db.requests.aggregate([ 
    {$project: {_id: 1, ward: 1, upvoted_by: 1}}, 
    {$unwind: "$upvoted_by" }, 
    {$group:{_id: {up:"$upvoted_by", ward: "$ward"}}}, 
    {$match: {"_id.ward": {$ne: null}}}, 
    {$group: {_id: "$_id.up",total: {"$sum":1}}},
    {$project: {"_id": {$toString: "$_id"}, total: "$total"}},
    {$sort: {total: -1}}, 
    {$limit: 50}
])


// With add to Set

db.requests.aggregate([
    {$project: {_id: 1, ward: 1, upvoted_by: 1}}, 
    {$unwind: "$upvoted_by"}, 
    {$group: {_id: "$upvoted_by", ward: {$addToSet: "$ward"}}}, 
    {$project: {upvoter: {$toString: "$_id"}, wards: {$size: "$ward"}}}, 
    {$sort: {ward: -1}}, 
    {$limit: 50}
])

