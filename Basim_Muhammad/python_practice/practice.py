# import random
# for i in range(1,1001):
# 	if i%2!=0:
# 		print i 

# i=5
# while i<1000001:
# 	print i
# 	i+=5


# a = [1, 2, 5, 10, 255, 3]
# sum=0
# for element in a:
# 	sum+=element
# print sum 

# a=[1,2,5,10,255,3]
# sum=0
# for element in a:
# 	sum+=element
# print sum/len(a)

# for num in xrange(1,2001):
# 	if num%2==0:
# 		print 'Number is', str(num) + '.This is an even number.'
# 	else:
# 		print 'Number is', str(num) + '.This is an odd number.'

# def times_five(arr):
# 	i=0
# 	for i in range(0,len(arr)):
# 		arr[i]=arr[i]*5
# 	return arr

# result=times_five([2,4,10,16])
# print result

# def grades():
# 	i=0
# 	for i in range(0,10):
# 		grade=raw_input('Enter your grade')
# 		grade=int(grade)
# 		if grade >89:
# 			print str(grade)+'; Your grade is A'
# 		elif grade >=80:
# 			print str(grade)+'; Your grade is B'
# 		elif grade >=70:
# 			print str(grade)+'; Your grade is C'
# 		elif grade >=60:
# 			print str(grade)+'; Your grade is D'
# 		else:
# 			print str(grade)+'; Your grade is F'
# 	print 'End of Program. Bye!'


# grades()

# def toss ():
# 	heads=0
# 	tails=0
# 	for i in range(1,5001):
# 		x=random.random()
# 		if round(x)==0:
# 			tails+=1
# 		else:
# 			heads+=1
# 	print 'Heads:',str(heads), 'Tails:', str(tails)

# toss()

# def draw_stars(arr):
# 	for num in arr:
# 		if type(num)==int:
# 			print '*'*num
# 		else:
# 			print num[0]*len(num)

# draw_stars([4,'john',2,4])

# students = [ 
# 	 {'first_name':  'Michael', 'last_name' : 'Jordan'},
# 	 {'first_name' : 'John', 'last_name' : 'Rosales'},
# 	 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 	 {'first_name' : 'KB', 'last_name' : 'Tonel'}]


# for i in students:
# 	print i['first_name'],i['last_name']

# users = {
#  'Students': [ 
# 	 {'first_name':  'Michael', 'last_name' : 'Jordan'},
# 	 {'first_name' : 'John', 'last_name' : 'Rosales'},
# 	 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 	 {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
# 	 {'first_name' : 'Michael', 'last_name' : 'Choi'},
# 	 {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }
# 
# for keys,values in users.iteritems():
# 	print keys
# 	count=0
# 	for info in values:
# 		count+=1
# 		print count,info['first_name'],info['last_name'],'-',str(len(info['first_name'])+len(info['last_name']))

# import re

# def get_matching_words(regex):
#  words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

#  return [word for word in words if re.search(regex, word)]

# # print get_matching_words('v')
# # print get_matching_words('ss')
# # print get_matching_words('e$')
# # print get_matching_words('b.*b')
# # print get_matching_words('b.b')
# # print get_matching_words('b.*b')
# # print get_matching_words('aeiou')
# print get_matching_words('[regularexpressions]')


	