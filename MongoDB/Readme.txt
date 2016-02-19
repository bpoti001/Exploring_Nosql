Data files are taken from IMDB and parsed using imbdpy2sql.py parser 
more details at (http://www.cs.odu.edu/~bpotinen/NoSql/IMDbPY.pdf) and fed into PostgreSql

From PostgreSql pulled out data having "USA" in address field. 
To parse the output I have used parser.py

In MongoDB created a collection named "movie_data"

Data is imported into MongoDB.For import I have used mongo shell and written a java script file and exported with its count. 

To find the coordiantes of cities and distance between the cities I have used Geopy package in python and spinned up a locally greedy traveling sales man code with cost function 


distance from A to B /number of movies at B

Plotted the travelling sales man problem using matplolib

