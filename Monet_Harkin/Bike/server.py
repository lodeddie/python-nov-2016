# Monet Harkin - Bike OOP test


class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles= 0
	def displayInfo(self):
		print "Price: "+ str(self.price )
		print "Max speed: "+ str(self.max_speed)
		print "Miles: "+ str(self.miles)
	def ride(self):
		self.miles += 10
		print "Riding"
	def reverse(self):
		if self.miles >= 5:
			self.miles -= 5
		else:
			self.miles =0
		print "Reversing"

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "27mph")
bike3 = Bike(100, "10mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

print"*" * 50

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

print"*" * 50

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

