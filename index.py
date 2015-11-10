import urllib2
import random
import names
import time

for i in range(20000):

	t = random.randint(0,3)
	x = random.randint(0,len(names.names)-1)
	y = random.randint(0,len(names.names)-1)
	req = "http://www.guerradosbairros.pt/vote.php?email="+names.names[y].lower() + names.names[x].lower()+str(t)+str(y)+"@gmail.com&zone_id=EX"
	try:
		time.sleep(t)
		urllib2.urlopen(req)
		if i%100 == 0:
			print i,t
	except:
		print 'O Alvaro nao desiste!'