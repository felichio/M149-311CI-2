db.citizens.aggregate([{
    $match: {upvotes: {$exists: true}}}, 
    {$project: {name: 1, num_of_upvotes: {$size: "$upvotes"}}}, 
    {$sort: {num_of_upvotes: -1}}, 
    {$limit: 50}
])