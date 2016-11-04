a = [2,4,10,16]
def multiply(arr,x):
	for i in range (0, len(a)):
		arr[i]=arr[i]*x
	return a 
	
	
b= multiply(a,5)
print b