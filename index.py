import urllib2
import random
import names

for i in range(18990):

	x = random.randint(0,len(names.names)-1)
	y = random.randint(0,len(names.names)-1)
	req = "http://www.guerradosbairros.pt/vote.php?email="+names.names[y].lower() + names.names[x].lower()+str(x)+str(y)+"@gmail.com&zone_id=EX"
	urllib2.urlopen(req)
	if i%100 == 0:
		print i