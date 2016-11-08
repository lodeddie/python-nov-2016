from Animal import Animal
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)
	def pet(self):
		self.health += 5
		return self
		
Dog("Rover").walk().walk().walk().run().run().pet().displayHealth()


		