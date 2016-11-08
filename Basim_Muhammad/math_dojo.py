class MathDojo(object):
	def __init__(self):
		self.result=0

	def add(self,*num2):
		count=0
		for i in num2:
			if type(i)==int:
				self.result+=i
				count+=1
			else:
				for element in i:
					self.result+=element
					count+=1
		print self.result
		return self
	def subtract(self,*num2):
		count=0
		for i in num2:
			if type(i)==int:
				self.result-=i
				count+=1
			else:
				for element in i:
					self.result+=element
					count+=1
		print self.result
		return self
	def result(self):
		print self.result
		return self

math=MathDojo()
math.add(2).add(2,5).subtract(3,2)

# math.add(2,5)
# math.subtract(3,2)

# md=MathDojo()

# md.add(2).result