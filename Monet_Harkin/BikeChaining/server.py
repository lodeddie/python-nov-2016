# Monet Harkin - Bike Chaining OOP test


class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles= 0
	def displayInfo(self):
		print "Price: "+ str(self.price )
		print "Max speed: "+ str(self.max_speed)
		print "Miles: "+ str(self.miles)
		print"*" * 50
		return self
	def ride(self):
		self.miles += 10
		print "Riding"
		return self
	def reverse(self):
		if self.miles >= 5:
			self.miles -= 5
		else:
			self.miles =0
		print "Reversing"
		return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "27mph")
bike3 = Bike(100, "10mph")

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()

