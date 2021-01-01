db.citizens.aggregate([
    {$match: {upvotes: {$exists: true}}}, 
    {$project: {_id: 1, name: 1, num_of_upvotes: {$size: "$upvotes"}}}, 
    {$sort: {num_of_upvotes: -1}}, 
    {$limit: 50}
])

// New implemenation

db.citizens.aggregate([
    {$match: {upvotes: {$exists: true}}}, 
    {$project: {_id: {$toString: "$_id"}, name: 1, num_of_upvotes: {$size: "$upvotes"}}}, 
    {$sort: {num_of_upvotes: -1}}, 
    {$limit: 50}
])