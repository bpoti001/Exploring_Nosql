import happybase
import csv

connection = happybase.Connection(host='localhost',port =9999)
t = connection.table('bpotinen')

data_d=[]
for k,v in t.scan(columns=['d']):
	data_d.append([k,len(v)])
	
with open('/root/nosql/out/d.csv','w') as f:
    for s in data_d:
            f.write(str(s[0])+','+str(s[1]) + '\n')

data_cc=[]

for k,v in t.scan(columns=['cc']):
	data_cc.append([k,len(v)])

with open('/root/nosql/out/cc.csv','w') as f:
    for s in data_cc:
            f.write(str(s[0])+','+str(s[1]) + '\n')
