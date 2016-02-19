import happybase
import csv
from itertools import *
connection = happybase.Connection(host='localhost',port =9999)
t = connection.table('bpotinen')
f = open('/root/nosql/data/movie_credit_requried.csv')
csv_f = csv.reader(f)
data=[]
for row in csv_f:
    data.append(row)
data = sorted(data,key = lambda t:t[0])
jj={}
for i in data:
        if i[0] in jj:
                jj[i[0]].append(i[1])
        else:
                jj[i[0]]=[i[1]]
for k,v in jj.items():
        for i in range(len(v)):
                t.put(k,{'cc:key%s'%i:v[i]})
f.close()
print "updpate cc family"

f = open('/root/nosql/data/mv_d.csv')
csv_f = csv.reader(f)
data=[]
for row in csv_f:
    data.append(row)
data = sorted(data,key = lambda t:t[0])
jj={}
for i in data:
        if i[0] in jj:
                jj[i[0]].append(i[1])
        else:
                jj[i[0]]=[i[1]]
for k,v in jj.items():
        for i in range(len(v)):
                t.put(k,{'d:key%s'%i:v[i]})
f.close()
print "updated d family"
