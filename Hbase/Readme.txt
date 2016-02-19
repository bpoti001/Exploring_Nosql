Pre-Processing:
The datafiles are available in IMDB datasets. All the .gz files were been set as input to imdbpy2sql.py available in (http://imdbpy.sourceforge.net/docs/README.sqldb.txt)

This Imdb parser will create a treditional database of IMDB, I have used PostgreSql as a base to get the 
requried data.


From the traditional database I pulled out two datafiles 
one with movie ids and its crazy credits and 
other with movie ids which has crazy credits and its directors

Using Hbase I tried to get the count of crazy credits avaiable in the database with respestive directors and moives. 

In HBase i created a table with two column families. 
To create this I used create.py script 
To run this script thrift server with port 9999 must be up and running 
	python create.py

then the two csv files were loaded into Hbase using load.py script. 
	python load.py

After loading count of crazy credits and the count of directores are fetched and writen to two different files using fetch.py
	python fetch.py

Using the output data I have plotted the Histogram using python matplotlib. The ipython file is attched in the pdf

Finally to delete the table, use delete.py script
	python delete.py