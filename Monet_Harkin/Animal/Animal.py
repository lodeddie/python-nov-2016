class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "Name: " + self.name 
		print "Health: " + str(self.health)

animal = Animal("Monkey", 100)

animal.walk().walk().walk().run().run().displayHealth()



