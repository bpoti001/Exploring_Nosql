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

for j in d_s:
	for i in data:
		if i[0] ==j:
			if i[1] in r.hkeys(j):
				r.hincrby(j,i[1],amount = 1)
			else:
				r.hmset(j,{i[1]:1})
