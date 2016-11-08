# Monet Harkin - Python/Advanced: MathDojo

# Part 1

print "*"*15 + "  Part 1  " + "*"*15

class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.total = 0

	def result(self):
		print "________"
		print self.total

	def add(self, *parm):
		for x in xrange(0,len(parm)):
			print "+"	
			print parm[x]
			self.total += parm[x]
		return self

	def subtract(self, *parm):
		for x in xrange(0,len(parm)):
			self.total -= parm[x]
			print"-"
			print parm[x]
		return self


MathDojo().add(2, 5).add(3).subtract(4).result()	

print "*"*10 + "Two samples of Part 1"

md = MathDojo().add(2).add(2,5).subtract(3,2).result()

print "*"*15 + "  Part 2  " + "*"*15


#Part 2


class MathDojo2(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.total = 0
		self.spot1 = ", "
		self.spot2 = ","
		self.inner_list = []
		self.inner_list2 = []

	def result(self):
		print "________"
		print self.total

	def add(self, *parm):
		if len(self.inner_list2) > 0:
			parm = self.inner_list2
			self.inner_list =[]
		for x in xrange(0,len(parm)):	
			if type(parm[x]) != int:
				self.inner_list += parm[x]
				continue
			print "+ " + str(parm[x])
			self.total += parm[x]
		self.inner_list2 =[]
		if len(self.inner_list)>0:
			self.add2(self.inner_list)
		return self

	def add2(self, *parm):
		parm = parm[0]
		for x in xrange(0,len(parm)):	
			if type(parm[x]) != int:
				self.inner_list2 += parm[x]
				continue
			self.total += parm[x]
			print "+ " +str(parm[x])
		self.inner_list =[]
		if len(self.inner_list2)>0:
			self.add(self.inner_list2)

	def subtract(self, *parm):
		if len(self.inner_list2) > 0:
			parm = self.inner_list2
		for x in xrange(0,len(parm)):	
			if type(parm[x]) != int:
				self.inner_list += parm[x]
				continue
			print "- " + str(parm[x])
			self.total -= parm[x]
		self.inner_list2 = []
		if len(self.inner_list)>0:
			self.subtract2(self.inner_list)
		return self

	def subtract2(self, *parm):
		parm = parm[0]
		for x in xrange(0,len(parm)):	
			if type(parm[x]) != int:
				self.inner_list2 += parm[x]
				continue
			print "- " + str(parm[x])
			self.total -= parm[x]
		self.inner_list =[]
		if len(self.inner_list2)>0:
			self.subtract(self.inner_list2)
		

MathDojo2().add([2,[5,6,4],10], 5).add(3).subtract(4,[2,[2,1],1]).result()