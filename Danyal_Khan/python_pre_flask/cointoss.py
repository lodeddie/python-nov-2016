import random

def coinToss(b):
	head_count=0
	tail_count=0
	for x in range(1,b+1):
		random_num = random.random()
		coin = round(random_num)
		if coin == 0:
			toss="head"
			head_count+=1
		else: 
			toss="tail"
			tail_count+=1
		print "attempt #" + str(x) + ": Throwing a coin... It's a " + toss + "! ... got " + str(head_count) + "head(s) so far and " + str(tail_count) + " tail(s) so far"

coinToss(5000)

