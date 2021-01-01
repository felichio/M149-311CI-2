db.citizens.aggregate([
    {$group: {_id: "$telephone", persons: {$sum: 1}, requests: {$push: "$upvotes"}}},
    {$project: {_id: 1, persons: 1, requests: 1, requests_temp: {$reduce: {input: "$requests", initialValue: [], in: {$concatArrays: ["$$value", "$$this"]}}}}}, 
    {$project: {_id: 1, persons: 1, requests: {$setIntersection: ["$requests_temp"]}}}, 
    {$match: {persons: {$gte: 2}}}, 
    {$group: {_id: null, requests: {$push: "$requests"}}}, 
    {$project: {requests: {$concatArrays: "$requests"}}}
])
// Wrong implementation
// No phone duplicate phone numbers ??


// New implementation
// WRONG
db.citizens.aggregate([
    {$group: {_id: "$telephone", persons: {$sum: 1}, requests: {$push: "$upvotes"}}}, 
    {$match: {persons: {$gte: 2}}}, 
    {$project: {_id: 1, persons: 1, requests: 1, requests_temp: {$reduce: {input: "$requests", initialValue: [], in: {$concatArrays: ["$$value", "$$this"]}}}}}, 
    {$project: {_id: 1, persons: 1, requests: {$reduce: {input: "$requests", initialValue: "$requests_temp", in: {$setIntersection: ["$$value", "$$this"]}}}}}, 
    {$project: {_id: 1, persons: 1, requests: {$map: {input: "$requests", as: "t", in: {$toString: "$$t"}}}}}
])

// New implemetation
db.citizens.aggregate([
    {$group: {_id: "$telephone", persons: {$sum: 1}, requests: {$push: "$upvotes"}}},
    {$match: {persons: {$gte: 2}}},
    {$unwind: "$requests" },
    {$unwind: "$requests" },
    {$group: {_id: {tel: "$_id", requests: "$requests"}, num_dup: {$sum: 1}}},
    {$match: {num_dup: {$gte: 2}}},
    {$project: {_id: 0, telephone: "$_id.tel", request: {$toString: "$_id.requests"}, num_dup: "$num_dup"}}
])