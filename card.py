from random import shuffle

class Card:

	def __init__(self, v, p):
		self.value = v
		self.naipe = p

	def get_value(self):
		return self.value

	def get_naipe(self):
		return self.naipe

	def get(self):
		return (self.value, self.naipe)
