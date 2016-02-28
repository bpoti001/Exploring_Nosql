Using CouchDB on IMDB dataset I plotted histogram of triva entries per movie 
and plotted a timeseries graph for 
	1) number of movies made that year / total number of movies till now 
	2) % movies made that year that has trivia count. 

For this again I used postgreSql to extract movies which has triva information and all movies with it's year.

These CSV files were converted to Json using CSV2JSON.py and used Blukload to load the data into CouchDB

Used Python+CouchDB to pull out the requried Count. 

query.py gives out below 3 files. 


count_of_count_of_triva.csv ==> contains count and its occurrence
percentages_of_movies_per_year.csv ==> contains % of movies released per year. 
percentages_of_triva_w.r.t_mv.csv ==> contains % of movies which have trivia info per year. 

These files are used with matl=plotlib to plot the required infromation

![Alt Text](https://github.com/bpoti001/Exploring_Nosql/raw/master/CouchDB/results_images/file-page1.jpg)
![Alt Text](https://github.com/bpoti001/Exploring_Nosql/raw/master/CouchDB/results_images/file-page2.jpg)
