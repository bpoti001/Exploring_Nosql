from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import itertools
import pprint
geolocator = Nominatim()
f = open('/root/nosql/ass4/fresh/final/check.out','r')
w = []
for row in f:
	w.append(row.strip().split("|"))
city = []
for i in w:
	city.append(i[0])
#print city
#for i in city:
#	if i =='center':
		
city[2]='Geographic Center of the Conterminous United States'
print city
dict ={}
for i in city:
	location = geolocator.geocode(i)
	dict[i] = [location.latitude, location.longitude]

diclist=[]
for k,v in dict.iteritems():
	temp=[k,v]
	diclist.append(temp)

per = []
for i in itertools.permutations(diclist, 2):
	per.append(i)

distance = []
for i in per:
	mile = vincenty(i[0][1],i[1][1]).miles
	distance.append([i[0][0],i[1][0],mile])

count=[]
for i in w:
	count.append([i[0],i[2]])

#for i in count:
#	if i[0]=='center':
#		i[0]= 'Geographic Center of the Conterminous United States'
count[2][0]='Geographic Center of the Conterminous United States'
co = {}
for i in count:
	co[i[0]]=i[1]
cost=[]
for i in distance:
	if i[1] in co:
		cost.append([i[0],i[1],float(i[2])/int(co[i[1]])])

v = ['Los Angeles']
max = 100
dum = 'a'
for j in range(len(city)):
	for i in cost:
		if i[0] ==v[len(v)-1] and i[2] <max and i[1] not in v:
			max = i[2]
			dum = i[1]
	v.append(dum)
	max = 100
	print v
	if len(v)==10:
		break

v.append('Los Angeles')
print v
for i in v:
	print i,dict[i]
