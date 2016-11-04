number="Number is"
even='this is an even number.'
odd='this is an odd number.'

for count in range(1,2001):
	if count%2 ==0:
		print number, count, even
	else:
		print number, count, odd
