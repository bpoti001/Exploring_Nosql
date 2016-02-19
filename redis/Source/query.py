import redis
import csv
f = open('/root/nosql/ass7/parse/final_let.csv')
data=[]
for line in f:
	d,m = line.strip().split(',')
	data.append([d,m])

d = []
for i in data:
	d.append(i[0])

d_s = set(d)

r = redis.StrictRedis(host='localhost', port=6379, db=0)
c = csv.writer(open("plot.csv", "w"))
for d in d_s:
		for m in r.hkeys(d):
			c.writerow([d,m,r.hmget(d,m)[0]]) 
