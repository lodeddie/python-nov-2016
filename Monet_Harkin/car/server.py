
class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

	def tax_percent(self):
		if self.price > 10000:
			tax = "0.15"
		else:
			tax = "0.12"
		return tax
	def display_all(self):
		print "Price: "+ str(self.price)
		print "Speed: "+ str(self.speed)
		print "Fuel: "+ str(self.fuel)
		print "Mileage: "+ str(self.mileage)
		print "Tax: "+ self.tax_percent()
		print "*"*50

ford = Car(20000, "100mpg", "Full", "15mpg")
chevy = Car(25000, "90mpg", "Not Full", "20mpg")
vw = Car(2000, "60mpg", "Full", "10mpg")
bmw = Car(5000, "70mpg", "Kinda Full", "20mpg")
dodge = Car(10000, "8mpg", "Not Full", "11mpg")
volvo = Car(11000, "50mpg", "Empty", "25mpg")

ford.display_all()
chevy.display_all()
vw.display_all()
bmw.display_all()
dodge.display_all()
volvo.display_all()

		