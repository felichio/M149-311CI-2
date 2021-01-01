db.citizens.aggregate([
    {$group: {_id: "$telephone", persons: {$sum: 1}, requests: {$push: "$upvotes"}}}, 
    {$project: {_id: 1, persons: 1, requests: {$setIntersection: "$requests"}}}, 
    {$match: {persons: {$gte: 2}}}, 
    {$group: {_id: null, requests: {$push: "$requests"}}}, 
    {$project: {requests: {$concatArrays: "$requests"}}}
])
// Wrong implementation
// No phone duplicate phone numbers ??


// New implementation

db.citizens.aggregate([
    {$group: {_id: "$telephone", persons: {$sum: 1}, requests: {$push: "$upvotes"}}}, 
    {$match: {persons: {$gte: 2}}}, 
    {$project: {_id: 1, persons: 1, requests: 1, requests_temp: {$reduce: {input: "$requests", initialValue: [], in: {$concatArrays: ["$$value", "$$this"]}}}}}, 
    {$project: {_id: 1, persons: 1, requests: {$reduce: {input: "$requests", initialValue: "$requests_temp", in: {$setIntersection: ["$$value", "$$this"]}}}}}, 
    {$project: {_id: 1, persons: 1, requests: {$map: {input: "$requests", as: "t", in: {$toString: "$$t"}}}}}
])