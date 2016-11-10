from Animal import Animal

class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)
	def fly(self):
		self.health -=10
		return self
	def displayHealth(self):
		print "This is a Dragon!"
		super(Dragon,self).displayHealth()
		

Dragon("Blaze").walk().walk().walk().run().run().fly().fly().displayHealth()
		