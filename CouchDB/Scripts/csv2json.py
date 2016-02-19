import csv
import json
csvfile = open('/home/bpotinen/nosql/ass5/csv_pgrs/csv/triva_year.csv','r')
jsonfile = open('/home/bpotinen/nosql/ass5/triva_year.json','w')
fields = ("movie_id","trivia","year")
reader = csv.DictReader(csvfile,fields)
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write(','+'\n')
