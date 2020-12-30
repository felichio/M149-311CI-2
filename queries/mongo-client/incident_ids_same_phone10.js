db.citizens.aggregate([
    {$group: {_id: "$telephone", persons: {$sum: 1}, requests: {$push: "$upvotes"}}}, 
    {$project: {_id: 1, persons: 1, requests: {$setIntersection: "$requests"}}}, 
    {$match: {persons: {$gte: 2}}}, 
    {$group: {_id: null, requests: {$push: "$requests"}}}, 
    {$project: {requests: {$concatArrays: "$requests"}}}
])

// No phone duplicate phone numbers ??