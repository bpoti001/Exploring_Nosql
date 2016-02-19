import couchdb
import json
import csv
couch = couchdb.Server()
db = couch['teja_2']
map_fun = '''function(doc) {
       emit(doc.movie_id,1);
 }'''
c = []
for row in db.query(map_fun,'_count',group=True):
	c.append(row)
t_c={}
for i in c:
	if i.value in t_c:
		t_c[i.value]=t_c[i.value]+1
	else:
		t_c[i.value]=1

t = []
for k,v in t_c.items():
	t.append([k,v])
with open("count_of_count_of_triva.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(t)


out=[]
year_c={}

map_fun_2 = '''function(doc) {
       emit([doc.year,doc.movie_id],1);
 }'''

for row in db.query(map_fun_2,'_count',group=True):
	out.append(row)
for i in out:
	if i.key[0] in year_c:
		year_c[i.key[0]]=year_c[i.key[0]]+1
	else:
		year_c[i.key[0]]=1	

m = []
for k,v in year_c.items():
	m.append([k,v])
with open("count_tirva_per_year.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(m)

map_fun_mv = '''function(doc) {
       emit(doc.year,1);
 }'''

db1 = couch['teja']
mv_c=[]
for row in db1.query(map_fun_mv,'_count',group=True):
	mv_c.append(row)
percentge = {}
for i in mv_c:
	percentge[i.key]=(i.value*100)/848549
p = []
for k,v in percentge.items():
	p.append([k,v])
with open("percentages_of_movies_per_year.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(p)
movies_year = {}
triva_year = {}
for i in mv_c:
	movies_year[i.key]=i.value
for j in m:
	triva_year[j[0]]=j[1]
mv_y = movies_year.keys()
t_y = triva_year.keys()
print ("length of mv_y",len(mv_y))
print ("length of t_vy",len(t_y))
tv_p=[]
for i in mv_y:
	if i in t_y:
		tv_p.append([i,(triva_year[i]/movies_year[i])*100])
	else:
		tv_p.append([i,0])
with open("percentages_of_triva_w.r.t_mv.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(tv_p)

