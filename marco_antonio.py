import urllib2
import random
import names
for i in range(200000):

	x = random.randint(0,len(names.names)-1)
	y = random.randint(0,len(names.names)-1)
	req = "http://www.guerradosbairros.pt/vote.php?email="+names.names[y].lower() + names.names[x].lower()+str(y)+str(x)+"@gmail.com&zone_id=EX"
	urllib2.urlopen(req)
	
	if i%1000 == 0:

		print 'mais '+str(i)+' cabrao!!!!'
	