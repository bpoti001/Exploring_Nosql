import csv
f = open('/home/bpotinen/nosql/ass4/scripts/submit/data/title_data.csv','r')
data =[]
for row in f:
	k,m,a= row.strip().split('|')
	data.append([k,m,a])

addr = []
for i in data:
	addr.append([i[0],i[1],i[2].split(',')])
req_add =[]
for	 i in addr:
	if len(i[2])==3:
		req_add.append([i[0],i[1],i[2]])
	if len(i[2])>3:
		req_add.append([i[0],i[1],i[2][-3:]])
	if len(i[2])==1 and i[2][0]=='USA':
		i[2].insert(0,'center')
		i[2].insert(0,'center')
		req_add.append([i[0],i[1],i[2]])
s=[]	
for i in req_add:
	s.append([i[0],i[1],i[2][0].strip(),i[2][1].strip(),i[2][2].strip()])

with open('/home/bpotinen/nosql/ass4/scripts/submit/data/title_out.csv',"w",newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['movie_id','title','city','state','country'])
	writer.writerows(s)
