import random
class Human(object):
	def __init__(self,clan=None):#none is default value for clan but we can change it.other attributs are hard-coded cant be changed
		print 'hey human'
		self.clan=clan # initialize more attributes that will be the same for all humans
		self.health=100
		self.strength=3
		self.intelligence=3
		self.stealth=3
	def taunt(self):
		print 'You want a piece of me'
	def attack(self):
		luck = round(random.random() * 100)
    	if(luck > 50):
      		if(luck * self.stealth > 150):
        		print 'attacking!'
        		return True
      		else:
        		print 'attack failed'
        		return False
    	else:
      		self.health -= self.strength 
      		print "attack failed"
      		return False


john=Human('CodingDojo')
print john.clan,john.stealth

# class Bike(object):
# 	def __init__(self,price,max_speed):
# 		self.price=price
# 		self.max_speed=max_speed
# 		self.miles=0
# 	def displayInfo(self):
# 		if self.miles>=0:
# 			print self.price,self.max_speed,self.miles
# 		else:
# 			self.miles=0
# 			print self.price,self.max_speed,self.miles
# 	def ride(self):
# 		print 'Riding'
# 		self.miles+=10
# 		return self
# 	def reverse(self):
# 		print 'Reversing'
# 		self.miles-=5
# 		return self
	


# mountain=Bike(300,50)
# dirt=Bike(700,85)
# motor=Bike(2000,5000)

# mountain.ride().ride().ride().reverse().displayInfo()

# motor.ride()
# motor.ride()
# motor.ride()
# motor.reverse()
# motor.displayInfo()

# class Car(object):
# 	def __init__(self,price,speed,fuel,mileage,tax=0.12):
# 		self.price=price
# 		self.speed=speed
# 		self.fuel=fuel
# 		self.mileage=mileage
# 		if self.price>10000:
# 			self.tax=0.15
# 		else:
# 			self.tax=0.12
# 		def displayAll(self,price,speed,fuel,mileage,tax):
# 			print '\n' + '\n' +'Price:'+ str(self.price) +'\n' + 'Speed'+self.speed +'\n' +'Fuel:' + self.fuel +'\n' +'Mileage:'+self.mileage+'\n' +'Tax Rate:'+str(self.tax)
# 		displayAll(self,price,speed,fuel,mileage,tax)
		
	

# mercedes=Car(10001,'200mph','full','25mpg')
# buick=Car(9999,'150mph','full','20mpg')

# nissan=Car(13500,'110mph','half','19mpg')
# subaru=Car(12890,'125mph','quarter','27mpg')
