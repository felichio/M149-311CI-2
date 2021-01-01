db.requests.aggregate([
    {$match: {creation_date: {$eq: ISODate("2016-05-18")}}}, 
    {$match: {upvoted_by: {$exists: true}}}, 
    {$project: {_id: 1, upvotes: {$size: "$upvoted_by"}}},
    {$sort: {upvotes: -1}}, {$limit: 50}
])

// Date is parameter

// New implementation

db.requests.aggregate([
    {$match: {creation_date: {$eq: ISODate("2016-05-18")}}}, 
    {$match: {upvoted_by: {$exists: true}}}, 
    {$project: {_id: {$toString: "$_id"}, upvotes: {$size: "$upvoted_by"}}},
    {$sort: {upvotes: -1}}, {$limit: 50}
])