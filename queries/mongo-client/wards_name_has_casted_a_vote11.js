db.citizens.aggregate([
    {$match: {name:"Norma Fisher"}},
    {$lookup: {from: "requests", localField: "upvotes", foreignField: "_id", as: "upvotes"}},
    {$project: {_id: 1, name: 1, wards: "$upvotes.ward"}},
    {$project: {_id: 1, name: 1, wards: {$setIntersection: ["$wards"]}}}
])

// Name is parameter

db.citizens.aggregate([
    {$match: {name:"Norma Fisher"}},
    {$lookup: {from: "requests", localField: "upvotes", foreignField: "_id", as: "upvotes"}},
    {$project: {_id: 1, name: 1, wards: "$upvotes.ward"}},
    {$project: {_id: {$toString: "$_id"}, name: 1, wards: {$setIntersection: ["$wards"]}}}
])