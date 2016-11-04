def grading():
	for i in range(1,11):
		grade= input("Enter Your Test Score")
		if grade >=90:
			letter="A"
		elif grade <90 and grade >79:
			letter="B"
		elif grade <80 and grade >69:
			letter="C"
		else:
			letter="D"		
		print "Score: "+ str(grade) + "; Your Grade is "+ letter
grading()	
print "End of Program. Bye!"	


