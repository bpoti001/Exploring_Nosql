list_movies  =db.movie_data.aggregate(     
{ "$group": 
{"_id": {city:"$city",state:"$state"},         
"movies": { $addToSet:  "$title" }}}, 
{ $unwind: "$movies" }, 
{ "$group": 
{ "_id": {city:"$_id.city",state:"$_id.state"}, 
count: { $sum: 1 },"mv":{$addToSet:  "$movies" }}}, 
{$sort:{count:-1}},
{$limit:10});

list_movies = list_movies["result"];

for (var i=0; i < list_movies.length; i++){

	print(list_movies[i]["_id"]["city"] + "|" + list_movies[i]["_id"]["state"] + "|" + list_movies[i]["count"] + "|" + list_movies[i]["mv"]);	
}


