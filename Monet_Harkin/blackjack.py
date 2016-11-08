#Monet Harkin 

#Blackjack project in progress

import random

# Below a player is being dealt the first two cards in the deck.
# To make this more accurate for all players being added:
# I should probably eventually have deck created and pop the first card in main Blackjack object
# Then each player calls on that dwindeling deck for the next cards.
# Working that direction... 
#Logic so far working- for one player getting 2 cards from the top of the deck

class Player(object):
	"""docstring for ClassName"""
	def __init__(self, wealth):
		self.deck = Deck().shuffle(3)
		self.card = 0
		self.card1 = self.deal()
		self.card2 = self.deal()
		self.wealth = wealth
	def show(self):
		print "Card 1 and 2:"
		print self.card1
		print self.card2
	def deal(self):
		self.card = self.deck[0]
		self.deck.pop(0)
		print "Dealt card:"
		print self.card
		print "Next Card in Deck"
		print self.deck[0]
		print "Working"
		return self.card


# class Dealer(Player):
# 	"""docstring for Dealer"""
# 	def __init__(self, arg):
# 		super(Dealer, self).__init__()

# class Blackjack(object):
# 	def __init__(self):
# 		self.deck = Deck().shuffle(3)
		
	


	
#Below Deck created and shuffled

class Deck(object):
	def __init__(self):
		self.deck =[]
		self.card = 0
	def makeDeck(self):
		for i in xrange(0,4):
			if i == 0:
				card_suit = "Spade"
			elif i == 1:
				card_suit = "Club"
			elif i == 2:
				card_suit = "Heart"
			else:
				card_suit = "Diamond"
			for x in xrange(1,14):
				if x == 1:
					card_val = 1
					card_name = "Ace"
				elif x > 1 and x < 11:
					card_val = x
					card_name = str(x)
				elif x == 11:
					card_val = 10
					card_name = "Jack"
				elif x == 12:
					card_val = 10
					card_name = "Queen"
				else:
					card_val = 10
					card_name = "King"
				self.deck +=[{card_val, card_name, card_suit}]
		#above loads the deck
	# Shuffles the deck	
	def shuffle(self, times_shuffled):
		self.makeDeck()
		for x in xrange(0, times_shuffled):
			random.shuffle(self.deck)
		# calls for the deck to be created and then shuffles the deck
		return self.deck


# Prints 1 Player's cards and assigns starting Wealth to the Player()

print Player(200).show()




		
		